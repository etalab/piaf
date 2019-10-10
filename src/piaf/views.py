import json
from random import randint

from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from api.permissions import SuperUserMixin
from .models import Article, ParagraphBatch, Paragraph, Question, Answer


class IndexView(TemplateView):
    template_name = "piaf/index.html"


class AdminView(TemplateView, SuperUserMixin):
    template_name = "piaf/admin.html"
    count_inserted_articles = None

    def post(self, request, *args, **kwargs):
        content = request.FILES["file"].read()
        data = json.loads(content).get("data")
        for d in data:
            article = Article(name=d["title"])
            article.save()
            for (i, p) in enumerate(d["paragraphs"]):
                if i % 5 == 0:
                    batch = ParagraphBatch()
                    batch.save()
                Paragraph(batch=batch, article=article, text=p["context"]).save()
        self.count_inserted_articles = len(data)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_inserted_articles"] = self.count_inserted_articles
        return context


class ArticleApi(View):
    # Provide a randomly picked pending article.
    def get(self, request, *args, **kwargs):
        qs = ParagraphBatch.objects.filter(status="pending")
        batch = qs[randint(0, qs.count() - 1)]
        paragraphs = Paragraph.objects.filter(batch=batch)
        data = model_to_dict(batch.article, ("name",))
        data["paragraphs"] = [model_to_dict(p, ("text",)) for p in paragraphs]
        return HttpResponse(json.dumps(data), content_type="application/json")

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        paragraph = Paragraph.objects.get(pk=data["paragraph"])
        for qa in data["data"]:
            question = Question(paragraph=paragraph, text=qa["question"])
            question.save()
            answer = Answer(
                question=question,
                text=qa["answer"]["text"],
                start_position=qa["answer"]["index"],
            )
            answer.save()
        paragraph.batch.status = 'complete'
        paragraph.batch.save()
        return HttpResponse(status=201)
