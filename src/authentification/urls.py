from django.urls import path
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetView, LogoutView

from .views import SignupView, LoginView
from .utils import activate


urlpatterns = [
    path('password_reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('activate/<str:uidb64>/<str:token>', activate, name='activate'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset")
]
