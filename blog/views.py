from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello world</h1>")
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts' : posts })