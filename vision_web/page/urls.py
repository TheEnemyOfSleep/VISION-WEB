from django.urls import path

from page.views import index_page

app_name = "block_list"

urlpatterns = [
    path('', index_page, name='index'),
]
