from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import TemplateView

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


def home(request):
    posts = Post.objects.all() 
    return render(request, 'blog/home.html', {'posts': posts})
    
class AboutView(TemplateView):

    template_name = 'blog/about.html'


class ContactView(TemplateView):

    template_name = 'blog/contact.html'
