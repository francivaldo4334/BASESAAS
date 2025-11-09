from rest_framework import serializers

from hello.models import HelloWorld


class HelloWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloWorld
        exclude = []
