from django.urls import path

from .views import IndexView, ParagraphApi, AdminView

app_name = "app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin", AdminView.as_view(), name="admin"),
    path("api/paragraph", ParagraphApi.as_view(), name="api_paragraph"),
]
