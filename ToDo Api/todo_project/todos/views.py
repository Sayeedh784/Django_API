from django.shortcuts import render
from rest_framework import generics, serializers
from .models import *
from . serializers import TodoSerializer
# Create your views here.

class ListTodo(generics.ListAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer