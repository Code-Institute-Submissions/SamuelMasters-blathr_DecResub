from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth.models import User



def home(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'post_list': post_list, 'category_list': category_list})


def add_post(request, form=PostForm):

    def get_form_kwargs(self):
        kwargs = super(add_post, self).get_form_kwargs
        kwargs['request'] = self.request
        return kwargs

    if request.POST:
        new_post = form(request.POST)
        print("DEBUG: request was recognised as POST.")

        if new_post.is_valid():
            print("DEBUG: new_post was recognised as valid.")
            new_post.author = request.user
            print("DEBUG: new_post.author id set to " + str(request.user.id))  # debug
            print("DEBUG: new_post.author username set to " + str(request.user.username))  # debug
            print("DEBUG: new_post.author is currently: " + str(new_post.author))  # debug
            print("DEBUG: printing new_post object...")
            print(new_post)
            new_post.save()
        redirect(home)

    current_user_id = request.user.id  # debug
    current_user_username = request.user.username  # debug
    print("DEBUG: current_user_id set to: " + str(current_user_id))  # debug
    print("DEBUG: current_user_username set to: " + current_user_username)  # debug

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
