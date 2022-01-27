from django.urls import include, path
from rest_framework import routers
from . import api


router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]