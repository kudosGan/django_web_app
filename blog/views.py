from django.shortcuts import render

posts = [{
    'author': 'kudosGan',
    'title': 'Blog Post 1',
    'content': 'first post content',
    'date_posted': 'August 28,2018'
}, {
    'author': 'kudosGan2',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'August 28, 2018'
}]

# Create your views here.


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def projects(request):
    return render(request, 'blog/projects.html', {'title': 'Projects'})


def chatbot(request):
    return render(request, 'blog/chatbot.html', {'title': 'ChatBot'})