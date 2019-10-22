from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path("", include("authentification.urls")),
    path("", include("server.urls")),
    path("", RedirectView.as_view(url="/app"), name="index"),
    path("app/", include("piaf.urls", namespace="app")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("v1/", include("api.urls")),
]

if "cloud_browser" in settings.INSTALLED_APPS:
    urlpatterns.append(path("cloud-storage/", include("cloud_browser.urls")))
