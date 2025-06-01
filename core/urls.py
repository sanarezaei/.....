from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView, ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls))
]