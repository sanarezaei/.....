from django.urls import path

from .views import RegisterApiView, LoginApiView, RefreshTokenApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name="register"),
    path('login/', LoginApiView.as_view(), name="login"),
    path('refresh/', RefreshTokenApiView.as_view(), name="refresh")
]