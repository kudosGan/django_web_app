from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('projects/', views.projects, name='blog-projects'),
    path('chatbot/', views.chatbot, name='blog-chatbot'),
]