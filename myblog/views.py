from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myblog/post_list.html', {'posts': posts}) 



