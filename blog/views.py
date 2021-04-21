from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.utils import timezone

def post_list(request):
    posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',  {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
