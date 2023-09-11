from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        user.set_password(validated_data.get('password'))
        user.save()

        return user


class UserAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class CurrentUserSerializer(serializers.ModelSerializer):
    pass