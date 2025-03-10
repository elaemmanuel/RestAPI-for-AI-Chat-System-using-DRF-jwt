from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser, UserProfile, Chat

class UserSerializer(serializers.ModelSerializer):
    #Serializer for CustomUser model, handles user creation.
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = make_password(validated_data.pop('password'))
        user = CustomUser.objects.create(username=validated_data['username'], password=password)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    #Serializer for UserProfile model.
    class Meta:
        model = UserProfile
        fields = ()

class RegisterSerializer(serializers.Serializer):
    #Serializer for user registration.
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        UserProfile.objects.create(user=user)
        return user

class ChatSerializer(serializers.ModelSerializer):
    #Serializer for Chat model.
    class Meta:
        model = Chat
        fields = '__all__'