from django.urls import path

from .views import LoginRegisterView, RefreshTokenApi

urlpatterns = [
    path('register/', LoginRegisterView.as_view(), name="register"),
    # path('login/', LoginApiView.as_view(), name="login"),
    path('refresh/', RefreshTokenApi.as_view(), name="refresh"),
    # path('password/reset/', PasswordResetRequestView.as_view(), name="password-reset"),
    # path('password/reset/confirm/', PasswordConfirmRequestView.as_view(), name="password-reset-confirm")
]