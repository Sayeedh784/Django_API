from django.urls import path
from .views import *


urlpatterns=[
  path('<int:pk>/',DetailTodo.as_view(),name='detail'),
  path('',ListTodo.as_view(),name='list'),
]
