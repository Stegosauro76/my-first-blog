from django.urls import path
from .views import post_list, post_detail, home, AboutView, ContactView

urlpatterns = [
    path('post', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('', home, name='home'),
    path('about/', AboutView.as_view(), name='about'),

    path('contact/', ContactView.as_view(), name='contact'),
]
