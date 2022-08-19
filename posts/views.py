from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import Post, Category
from .forms import PostForm


def home(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'post_list': post_list, 'category_list': category_list})


def add_post(request):
    if request.POST:
        new_post = PostForm(request.POST)
        print(request.POST)  # debug statement, remove before final deploy
        if new_post.is_valid():
            new_post.save()
        redirect(home)
    current_user = request.user
    print(current_user.username)  # debug
    return render(
        request,
        'add.html',
        {
            "post_form": PostForm(),
            "current_user": current_user,
        },
    )


# class Homepage(generic.ListView):

#     model = Post
#     post_list = Post.objects.all()
#     category_list = Category.objects.all()
#     template_name = 'index.html'
