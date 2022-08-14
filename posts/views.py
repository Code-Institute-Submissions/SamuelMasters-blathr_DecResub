from django.shortcuts import render
from django.views import View, generic
from .models import Post, Category


def home(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'post_list': post_list, 'category_list':category_list})


# class Homepage(generic.ListView):

#     model = Post
#     post_list = Post.objects.all()
#     category_list = Category.objects.all()
#     template_name = 'index.html'
