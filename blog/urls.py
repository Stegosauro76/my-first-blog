from django.urls import path
from .views import post_list, post_detail, home

urlpatterns = [
    path('post', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('', home, name='home'),
]
