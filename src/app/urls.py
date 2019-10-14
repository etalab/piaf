from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import PasswordResetView, LogoutView, LoginView
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('authentification.urls')),
    path('', include('server.urls')),
    path('', RedirectView.as_view(url='/app'), name='index'),
    path('app/', include('piaf.urls', namespace='app')),
    path('admin/', admin.site.urls),
    path('social/', include('social_django.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/', include('api.urls')),
]

if 'cloud_browser' in settings.INSTALLED_APPS:
    urlpatterns.append(path('cloud-storage/', include('cloud_browser.urls')))
