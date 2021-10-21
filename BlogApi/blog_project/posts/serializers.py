from rest_framework import fields, serializers
from .models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'author', 'title', 'body', 'created_at',)
    model = Post

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('id','username',)