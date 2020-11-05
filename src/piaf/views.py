import json
from random import randint

from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

from api.permissions import SuperUserMixin
from .models import Article, ParagraphBatch, Paragraph, Question, Answer, UserRelevancy


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "front/index.html"


class AdminView(SuperUserMixin, TemplateView):
    template_name = "piaf/admin.html"


class AdminDatasetView(SuperUserMixin, TemplateView):
    template_name = "piaf/admin.html"
    count_inserted_articles = None

    def get(self, request, *args, **kwargs):
        data = []
        for article in (
            Article.objects.filter(paragraphs__status="completed")
            .prefetch_related("paragraphs__questions__answers")
            .distinct("id")
        ):
            paragraphs = []
            for paragraph in article.paragraphs.filter(status="completed"):
                questions = []
                for question in paragraph.questions.all():
                    q = {
                        "question": question.text,
                        "id": question.id,
                        "answers": [
                            {"text": a.text, "answer_start": a.index}
                            for a in question.answers.all()
                        ],
                    }
                    questions.append(q)
                p = {"context": paragraph.text, "qas": questions}
                paragraphs.append(p)
            d = {
                "title": article.name,
                "categorie": article.theme,
                "wikipedia_page_id": article.reference,
                "audience": article.audience,
                "paragraphs": paragraphs,
            }
            data.append(d)
        response = HttpResponse(
            json.dumps({"data": list(data), "version": "v1.0"}),
            content_type="application/json",
        )
        response["Content-Disposition"] = "attachment; filename=piaf-annotations.json"
        return response

    def post(self, request, *args, **kwargs):
        content = request.FILES["file"].read()
        data = json.loads(content).get("data")
        for d in data:
            name = d["displaytitle"] if "displaytitle" in d == True else d["title"]
            cat = d["categorie"] if "categorie" in d == True else "Société"
            ref = d["reference"] if "reference" in d == True else 0
            article = Article(
                name=name,
                theme=cat,
                reference=ref,
                audience=request.POST["audience"],
            )
            article.save()
            for (i, p) in enumerate(d["paragraphs"]):
                if i % 5 == 0:
                    batch = ParagraphBatch()
                    batch.save()
                paragraph=Paragraph(batch=batch, article=article, text=p["context"])
                paragraph.save()
                for question in p["qas"]:
                    Question(paragraph=paragraph, text=question["question"]).save()
        context = {"count_inserted_articles": len(data)}
        return self.render_to_response(context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_inserted_articles"] = self.count_inserted_articles
        return context


def get_datasets_info(request):
    theme = request.GET.get("theme")
    qs = Article.objects.distinct("pk")
    if theme:
        qs = qs.filter(theme=theme)
    if not request.user.is_certified:
        qs = qs.filter(audience="all")
    data = {
        "count_completed_articles": qs.exclude(paragraphs__status="pending").count(),
        "count_pending_articles": qs.filter(paragraphs__status="pending").count(),
    }
    return JsonResponse(data)


@method_decorator(csrf_exempt, name="dispatch")
class ParagraphView(View):
    def get(self, request, *args, **kwargs):
        """Provide a randomly picked pending article."""
        theme = request.GET.get("theme")
        qs = ParagraphBatch.objects.exclude(status="completed").distinct("id")
        # Limit display by audience
        if getattr(request.user, "is_certified", False):
            qs_certified = qs.filter(paragraphs__article__audience="restricted")
            if qs_certified.count():
                qs = qs_certified
        else:
            qs = qs.filter(paragraphs__article__audience="all")
        # Limit by theme
        if theme:
            qs = qs.filter(paragraphs__article__theme=theme)
        if not qs.count():
            return JsonResponse({})
        batch = qs.filter(status="progress", user=request.user).first()
        if not batch:
            batch = qs.filter(status="pending")[randint(0, qs.count() - 1)]
        article = batch.article
        paragraph = batch.paragraphs.filter(status="pending").first()
        data = {
            "id": paragraph.id,
            "theme": article.theme,
            "text": paragraph.text,
            "title": article.name,
            "count_pending_paragraphs": batch.paragraphs.filter(
                status="pending"
            ).count(),
            "count_pending_batches": article.batches.filter(status="pending").count(),
            "count_completed_paragraphs": batch.paragraphs.filter(
                status="completed"
            ).count(),
            "count_completed_batches": article.batches.filter(
                status="completed"
            ).count(),
            "count_progress_batches": article.batches.filter(status="progress").count(),
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        paragraph = Paragraph.objects.get(pk=data["paragraph"])
        paragraph.complete(data["data"], request.user)
        return JsonResponse(None, status=201, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class QuestionView(View):
    def get(self, request):
        user = request.user
        questions = (
            Question.objects.filter(status="pending")
            .exclude(paragraph__user=user)
            .exclude(answers__user=user)
            .annotate(answers_count=Count("answers"))
            .order_by("-answers_count")
        )
        count = questions.count()
        if count == 0:
            return JsonResponse({})
        question = questions[randint(0, count - 1)]
        paragraph = question.paragraph
        article = paragraph.article

        data = {
            "id": question.id,
            "text": question.text,
            "paragraph": {
                "id": paragraph.id,
                "theme": article.theme,
                "title": article.name,
                "text": paragraph.text,
            },
        }
        return JsonResponse(data)

    def post(self, request):
        data = json.loads(request.body)
        question = Question.objects.get(pk=data["id"], status="pending")
        Answer.objects.create(
            question=question, text=data["text"], index=data["index"], user=request.user
        )
        return JsonResponse(None, status=201, safe=False)

    def put(self, request):
        data = json.loads(request.body)
        question = Question.objects.get(pk=data["id"])
        question.report_increase()
        return JsonResponse(None, status=201, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserStepView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        level = int(data["level"])
        if level > user.level_completed + 1:
            return HttpResponse(
                f"Level {level} is not accessible for this user.", status=422
            )
        user.level_completed = level
        relevancy = UserRelevancy(score=data["score"], level=level, user=user)
        relevancy.save()
        user.relevancies.add(relevancy)
        user.save()
        data = {
            "level_completed": user.level_completed,
        }
        return JsonResponse(data, status=201)
