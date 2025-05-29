from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import AccountSerializer, ProfileSerializer
from .models import Account, Profile

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ProfileViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        profile = Profile.objects.get(account=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
