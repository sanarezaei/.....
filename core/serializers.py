from django.contrib.admin.utils import model_ngettext
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Profile


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            password2=validated_data['password2']
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['phone_number'] = user.phone_number
        return token


class ProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='user.profile_number', read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'phone_number', 'first_name', \
                  'last_name', 'bio', 'birth_date', 'avatar', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']