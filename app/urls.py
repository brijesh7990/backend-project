from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('profile', ProfileView, basename='profiles')



urlpatterns = [
    
]

urlpatterns += router.urls
