from django.urls import path
from .views import *
urlpatterns=[
  path('',BookApiView.as_view(),name='api'),
]