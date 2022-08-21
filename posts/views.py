from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth.models import User



def home(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'post_list': post_list, 'category_list': category_list})


def add_post(request, form=PostForm):

    if request.POST:
        new_post = form(request.POST)

        if new_post.is_valid():
            post_to_add = new_post.save(commit=False)
            post_user = User.objects.get(username=request.user.username)
            post_to_add.author = post_user  # adds the current user as author
            post_to_add.save()
            return redirect(home)  # redirects to home page after submission

    return render(
        request,
        'add.html',
        {
            "post_form": PostForm(),
        },
    )
