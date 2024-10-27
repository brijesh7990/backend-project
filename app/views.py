from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer
from .models import *
# Create your views here.


class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
