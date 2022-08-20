from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import Post, Category
from .forms import PostForm



def home(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'post_list': post_list, 'category_list': category_list})


def add_post(request, form=PostForm):

    if request.POST:
        new_post = form(request.POST)
        print("Request was recognised as POST.")

        if new_post.is_valid():
            print("new_post was recognised as valid.")
            new_post.author = request.user
            print("new_post.author id set to " + str(request.user.id))  # debug
            print("new_post.author username set to " + str(request.user.username))  # debug
            print("new_post.author is currently: " + str(new_post.author))
            new_post.save()
        redirect(home)

    current_user_id = request.user.id  # debug
    current_user_username = request.user.username  # debug
    print(current_user_id)  # debug
    print(current_user_username)  # debug

    return render(
        request,
        'add.html',
        {
            "post_form": PostForm(),
        },
    )


# class Homepage(generic.ListView):

#     model = Post
#     post_list = Post.objects.all()
#     category_list = Category.objects.all()
#     template_name = 'index.html'
