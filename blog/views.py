from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import TemplateView
from django.http import HttpResponse
from . import forms
from django.shortcuts import  redirect



def post_list(request):
    posts = Post.objects.all()
    # Assuming 'comment' is defined somewhere, otherwise this will raise an error
    # If you don't have comments, you can remove 'comments' from the context
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)  

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


def post_new(request):

    if request.method == 'POST':

        form = forms.CreatePost(request.POST)  # Crea un'istanza del modulo con i dati inviati

        if form.is_valid():  # Verifica se il modulo è valido

            post = form.save()  # Salva il nuovo post nel database

            return redirect('post_detail', post_id=post.id)  # Reindirizza al dettaglio del post appena creato

    else:

        form = forms.CreatePost()  # Crea un modulo vuoto per la visualizzazione iniziale


    return render(request, 'blog/post_edit.html', {'form': form})  # Rende la pagina con il modulo