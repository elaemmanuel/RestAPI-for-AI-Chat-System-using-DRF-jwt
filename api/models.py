from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #Custom User model extending AbstractUser with additional tokens field
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    tokens = models.IntegerField(default=4000)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    #UserProfile model to extend user information.
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    #Chat model to store chat history.
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} at {self.timestamp}"