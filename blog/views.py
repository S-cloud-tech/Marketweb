from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import *

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/posts/list.html'

# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 10)
#     page_number =request.GET.get('page', 1)
#     posts = paginator.get_page(page_number)
#     return render(request, 'blog/posts/list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/posts/detail.html',{'post': post})
