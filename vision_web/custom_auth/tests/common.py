from django.contrib.auth import get_user_model


def create_user(**param):
    return get_user_model().objects.create_user(**param)


def create_superuser(**param):
    return get_user_model().objects.create_superuser(**param)
