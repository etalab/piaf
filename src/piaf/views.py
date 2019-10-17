import json
from random import randint

from django.views.generic import TemplateView

from api.permissions import SuperUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, ParagraphBatch, Paragraph


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "piaf/index.html"


class AdminView(TemplateView, SuperUserMixin):
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
