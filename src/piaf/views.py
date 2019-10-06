import json
from random import randint

from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers

from api.permissions import SuperUserMixin
from .models import Article, Paragraph, Question, Answer


class IndexView(TemplateView):
    template_name = 'piaf/index.html'


class AdminView(TemplateView, SuperUserMixin):
    template_name = 'piaf/admin.html'
    count_inserted_articles = None

    def post(self, request, *args, **kwargs):
        content = request.FILES['file'].read()
        data = json.loads(content).get('data')
        for d in data:
            article = Article(name=d['title'])
            article.save()
            for p in d['paragraphs']:
                Paragraph(article=article, text=p['context']).save()
        self.count_inserted_articles = len(data)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_inserted_articles'] = self.count_inserted_articles
        return context


class ArticleApi(View):
    # Provide a randomly picked pending article.
    def dispatch(self, request, *args, **kwargs):
        qs = Article.objects.filter(status='pending')
        article = qs[randint(0, qs.count() - 1)]
        paragraphs = Paragraph.objects.filter(article=article)
        data = model_to_dict(article, ('name',))
        data['paragraphs'] = [model_to_dict(p, ('text',)) for p in paragraphs]
        return HttpResponse(json.dumps(data), content_type='application/json')
