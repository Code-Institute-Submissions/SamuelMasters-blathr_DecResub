from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Post, Category
from .forms import PostForm


def home(request):
    """
    View for the homepage of the site.
    """
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'post_list': post_list,
                                          'category_list': category_list})


def add_post(request, form=PostForm):
    """
    View for the post creation interface, and to add new posts to database.
    """

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

def post_detail(request, post_id):
    """
    View for showing one post in it's entirety.
    """
    context = {}

    context['data'] = Post.objects.get(post_id=post_id)

    return render(request, 'post_detail.html', context)


def delete_post(request, post_id):
    """
    View for deleting a post from the database.
    """
    post = Post.objects.get(post_id=post_id)
    post.delete()
    return redirect(home)


def edit_post(request, post_id):
    """
    View for updating a post.
    """
    post = Post.objects.get(post_id=post_id)
    template = loader.get_template('edit_post.html')
    context = {
        'post': post,
    }

    if request.POST:
        title = request.POST['post_title']
        content = request.POST['post_content']
        post = Post.objects.get(post_id=post_id)
        post.title = title
        post.content = content
        post.save()
        return redirect(home)

    return HttpResponse(template.render(context, request))


def update_post(request, post_id):
    """
    Updates records after edits are submitted.
    """
    title = request.POST['post_title']
    content = request.POST['post_content']
    post = Post.objects.get(post_id=post_id)
    post.title = title
    post.content = content
    post.save()
    return redirect(home)
