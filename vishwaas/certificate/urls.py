from rest_framework import routers
from django.urls import path
from .views import *


router = routers.DefaultRouter()
urlpatterns = [
    path('certificates', Certificate.as_view()),
    path('verify_certificate/<str:osid>', VerifyCertificate.as_view()), 
]
