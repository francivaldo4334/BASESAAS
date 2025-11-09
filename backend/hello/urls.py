from django.urls import include, path

from hello.views import HelloWorldViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(
    r"hello_world",
    HelloWorldViewSet,
    basename="hello_world",
)

urlpatterns = [
    path("", include(router.urls)),
]
