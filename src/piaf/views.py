import json
from random import randint

from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from api.permissions import SuperUserMixin
from .models import Article, ParagraphBatch, Paragraph


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "piaf/index.html"


class AdminView(SuperUserMixin, TemplateView):
    template_name = "piaf/admin.html"
    count_inserted_articles = None

    def post(self, request, *args, **kwargs):
        content = request.FILES["file"].read()
        data = json.loads(content).get("data")
        for d in data:
            article = Article(
                name=d["displaytitle"],
                theme=d["categorie"],
                reference=d.get("wikipedia_page_id"),
                audience=request.POST["audience"],
            )
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


@method_decorator(csrf_exempt, name="dispatch")
class ParagraphView(View):

    # Provide a randomly picked pending article.
    def get(self, request, *args, **kwargs):
        theme = request.GET.get("theme")
        qs = ParagraphBatch.objects.filter(status="pending")
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
        # Pick one batch, randomly
        batch = qs[randint(0, qs.count() - 1)]
        article = batch.article
        paragraph = batch.paragraphs.filter(status="pending").first()
        data = {
            "id": paragraph.id,
            "theme": article.theme,
            "text": paragraph.text,
            "title": article.name,
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        paragraph = Paragraph.objects.get(pk=data["paragraph"])
        paragraph.complete(data["data"], request.user)
        return JsonResponse(None, status=201, safe=False)
