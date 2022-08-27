from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from .models import Post, Category
from .forms import PostForm, CommentForm


def home(request):
    """
    View for the homepage of the site.
    """

    category_list = Category.objects.all()
    post_list = Post.objects.filter(status=1).order_by('-created_date')
    paginator = Paginator(post_list, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'post_list': post_list,
                                          'category_list': category_list,
                                          'page_obj': page_obj, })


def filtered_list(request, category_id):
    """
    Filtered view for the homepage of the site.
    """

    category_list = Category.objects.all()
    post_list = Post.objects.filter(category_id=category_id).order_by('-created_date')

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
            messages.add_message(request, messages.SUCCESS, 'Your post was submitted and is awaiting approval.')
            return redirect(home)  # redirects to home page after submission
        else:
            messages.add_message(request, messages.ERROR, 'There was a problem, please try submitting your post again.')

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

    post = Post.objects.get(post_id=post_id)
    comments = post.comments.filter(approved=True)
    print("request.method is " + request.method)

    if request.POST:
        comment_form = CommentForm(data=request.POST)
        print("The request.method was recognised as POST.")  # debug

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user.username
            new_comment.post = post
            messages.add_message(request, messages.SUCCESS, 'Your comment was submitted and is awaiting approval.')
            new_comment.save()
            print("The new_comment instance was saved.")  # debug
        else:
            comment_form = CommentForm()
            print("The comment form was rendered blank.")  # debug

    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'comments': comments,
            'comment_form': CommentForm(),
         },
          )


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
        post.status = 0  # Reset status to require admin reapproval
        post.save()
        return redirect(home)

    return HttpResponse(template.render(context, request))
