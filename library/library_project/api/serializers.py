from django.db.models import fields
from rest_framework import serializers
from books.models import *


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('title','subtitle','author','isbn')