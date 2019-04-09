from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    blogposts = Post.objects.all()
    return render(request, 'blog/post_list.html', {"Entries":blogposts})