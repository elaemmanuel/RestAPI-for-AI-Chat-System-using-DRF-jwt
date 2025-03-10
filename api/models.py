from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #Extends the built-in Django User model with additional user-specific data.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokens = models.IntegerField(default=4000)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    # Chat model to store chat history
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} at {self.timestamp}"
