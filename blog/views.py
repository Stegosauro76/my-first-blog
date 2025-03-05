from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import TemplateView
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.all()
    # Assuming 'comment' is defined somewhere, otherwise this will raise an error
    # If you don't have comments, you can remove 'comments' from the context
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

def contatto_view(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        messaggio = request.POST.get('message')
        
        # Logic to send email or save data
        # For example, you can use Django's Email functionality to send an email

        # After processing, you might want to redirect or render a success message
        return redirect('success_url')  # Replace 'success_url' with your actual URL name

    return render(request, 'blog/contact.html')
