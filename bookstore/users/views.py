from django.shortcuts import render, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

# Create your views here.

class Register_User(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get('username')

        if User.objects.filter(username=username).exists():
            return Response({'error':'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token, created = Token.objects.get_or_create(user=user)

            return Response({'token':token.key}, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class Login_User(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key}, status=status.HTTP_200_OK)

# class Logout_User(APIView):
    
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         request.user.auth_token_delete()

#         return Response({'message':'Logged out successfully'})
    

class Profile_View(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, profile_pk):
        
        user = User.objects.get_object_404(pk=profile_pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

