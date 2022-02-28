from django.shortcuts import render
from .models import Post

# Create your views here.


def home(req):

    all_posts = Post.objects.all()
    return render(req, 'index.html', {'posts': all_posts})
