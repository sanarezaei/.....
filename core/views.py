from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, \
    ProfileSerializer
from .models import User, Profile

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
