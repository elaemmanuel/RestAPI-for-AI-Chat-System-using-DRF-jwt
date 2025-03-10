from django.urls import path
from .views import register_user, login_user, chat, get_token_balance
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('chat/', chat, name='chat'),
    path('balance/', get_token_balance, name='balance'),
]