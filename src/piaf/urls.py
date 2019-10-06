from django.urls import path

from .views import IndexView, ArticleApi, AdminView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin', AdminView.as_view(), name='admin'),
    path('api/article', ArticleApi.as_view(), name='api_article'),
]
