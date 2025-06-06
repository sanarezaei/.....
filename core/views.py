from os import access

from pyexpat.errors import messages
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, RefreshTokenSerializer


class RegisterApiView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")

        if not phone or not password:
            return Response(
                {"detail": "شماره تلفن و پسورد الزامی هستند"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            if User.objects.filter(phone=phone).exists():
                return Response(
                    {"detail": "این شماره تلفن قبلا ثبت نام کرده است"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer = UserSerializer(data={"phone": phone, "password": password})
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(password)
                user.save()

                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "message": "ثبت نام موفقیت آمیز"
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"detail": "خطای سرور داخلی"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginApiView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")

        if not phone or not password:
            return Response({"detail": "شماره تلفن یا پسورد الزامی هستند"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone=phone)
            if not user.check_password(password):
                return Response({"detail": "پسورد اشتباه است"},
                                status=status.HTTP_400_BAD_REQUEST)

            access_token = str(RefreshToken.for_user(user).access_token)
            return Response({
                "access": access_token,
                "message": "رود موفقیت آمیز"
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "کاربر با این شماره تلفن وجود ندارد"},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"detail": "خطای سرور داخلی"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RefreshTokenApiView(APIView):
    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            refresh = RefreshToken(serializer.validated_data["refresh"])
            new_access_token = str(refresh.access_token)

            return Response({
                "access": new_access_token,
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "Refresh Token نامعتبر یا منقضی شده است"},
                            status=status.HTTP_401_UNAUTHORIZED)
