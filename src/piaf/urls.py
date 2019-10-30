from django.urls import path

from .views import IndexView, AdminView, AdminDatasetView, ParagraphView, get_datasets_info
from .apis import MeView


app_name = "app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin", AdminView.as_view(), name="admin"),
    path("admin/dataset", AdminDatasetView.as_view(), name="dataset"),
    path("api/datasets", get_datasets_info),
    path("api/paragraph", ParagraphView.as_view(), name="api_paragraph"),
    path("me", MeView.as_view(), name="me"),
]
