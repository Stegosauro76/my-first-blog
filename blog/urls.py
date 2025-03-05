from django.urls import path
from .views import post_list, post_detail, post_new, home, AboutView, ContactView,search_posts

urlpatterns = [
    path('post/', post_list, name='post_list'),  # Lista dei post
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # Dettagli del post
    path('', home, name='home'),  # Home page
    path('about/', AboutView.as_view(), name='about'),  # Pagina "Chi siamo"
    path('new/', post_new, name='post_new'),  # Crea un nuovo post
    path('contact/', ContactView.as_view(), name='contact'),  # Pagina di contatto
    path('search/', search_posts, name='search_posts'),
]