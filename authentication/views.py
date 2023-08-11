from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
