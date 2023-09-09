from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        mosel = User
        excluse = ('id',)


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password')
