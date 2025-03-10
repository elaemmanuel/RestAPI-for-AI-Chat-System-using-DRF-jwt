from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Chat
from django.contrib.auth.hashers import make_password


# Serializer for User model, handles user creation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        user = User.objects.create(username=validated_data['username'], password=password)
        return user


# Serializer for the UserProfile model, used to represent and validate token data
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('tokens',)


#Serializer for user registration
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    tokens = serializers.IntegerField(default=4000)

    #Creates a new User and UserProfile object during registration
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        UserProfile.objects.create(user=user, tokens=validated_data['tokens'])
        return user


# Serializer for Chat model, handles chat message data
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'