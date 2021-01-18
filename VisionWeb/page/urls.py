from django.urls import path

from page.views import BlockView

app_name = "block_list"

urlpatterns = [
    path('', BlockView.as_view(), name='index'),
]
