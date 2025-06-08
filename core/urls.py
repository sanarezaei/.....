from django.urls import path

from .views import RegisterApiView, LoginApiView, RefreshTokenApiView,\
    PasswordResetRequestView, PasswordConfirmRequestView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name="register"),
    path('login/', LoginApiView.as_view(), name="login"),
    path('refresh/', RefreshTokenApiView.as_view(), name="refresh"),
    path('password/reset/', PasswordResetRequestView.as_view(), name="password-reset"),
    path('password/reset/confirm/', PasswordConfirmRequestView.as_view(), name="password-reset-confirm")
]