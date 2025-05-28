from rest_framework import serializers
from .models import Account, Profile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        account = Account.objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            password2=validated_data['password2']
        )
        return account


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['account']