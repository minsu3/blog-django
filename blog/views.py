from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
  {
    'author': 'Minsu Kim',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 6, 2020'
  },
  {
    'author': 'Suyoung Min',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'March 7, 2018'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})