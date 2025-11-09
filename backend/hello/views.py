from django.shortcuts import render
from rest_framework import viewsets

from hello.models import HelloWorld
from hello.serializers import HelloWorldSerializer

# Create your views here.
class HelloWorldViewSet(viewsets.ModelViewSet):
    queryset = HelloWorld.objects.all()
    serializer_class = HelloWorldSerializer
