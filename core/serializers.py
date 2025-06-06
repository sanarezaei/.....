from enum import unique

from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'password', 'email','fullname', \
                  'gender', 'birth_date', 'image']
        extra_kwargs = {'password': {'write_only': True}}

class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)

    def validate_refresh(self, value):
        if not value:
            raise serializers.ValidationError("رفرش توکن نمیتواند خالی باشد")

        return value
