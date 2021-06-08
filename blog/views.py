from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def projects(request):
    return render(request, 'blog/projects.html', {'title': 'Projects'})


def chatbot(request):
    return render(request, 'blog/chatbot.html', {'title': 'ChatBot'})