from django.urls import re_path, include, path
from rest_framework import routers

from custom_auth.views import RegistrationAPIView
from custom_auth.views import LoginAPIView
from custom_auth.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    re_path(
        r'^registration/?$',
        RegistrationAPIView.as_view(),
        name='user_registration'
    ),
    re_path(
        r'^login/?$',
        LoginAPIView.as_view(),
        name='user_login'
    ),
]
