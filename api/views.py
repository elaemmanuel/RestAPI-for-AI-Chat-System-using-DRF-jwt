from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate
from .models import UserProfile, Chat
from .utils import send_code_to_api 
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
@permission_classes([AllowAny])
# Register a new user
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
#Login User
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    user_profile = UserProfile.objects.get(user=request.user)
    message = request.data.get('message')
    if user_profile.tokens < 100:
        return Response({'error': 'Insufficient tokens'}, status=status.HTTP_402_PAYMENT_REQUIRED)
    user_profile.tokens -= 100
    user_profile.save()
    response = send_code_to_api(message) 
    if response:
        Chat.objects.create(user=request.user, message=message, response=response)
        return Response({'response': response}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Chatbot error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_token_balance(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return Response({'tokens': user_profile.tokens}, status=status.HTTP_200_OK)
