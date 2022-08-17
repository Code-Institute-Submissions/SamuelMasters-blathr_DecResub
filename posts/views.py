from django.shortcuts import render
from django.views import View, generic
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category
from .forms import PostForm


def home(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'index.html', {'post_list': post_list, 'category_list': category_list})


# def add(request):
#     template = loader.get_template('add.html')
#     return HttpResponse(template.render({}, request))


# def add_post(request):
#     post_title = request.POST['post-title']
#     post_content = request.POST['post-content']
#     post_category = request.POST['post-category']
#     post_author = request.user
#     print(post_author)  # remove before final deploy
#     new_post = Post(title=post_title, author=post_author, content=post_content, category='Finance')
#     new_post.save()
#     return HttpResponseRedirect(reverse('index'))


def add_post(request):
    categories = Category.objects.all()

    return render(
        request,
        'add.html',
        {
            "post_form": PostForm()
        },
    )


# class Homepage(generic.ListView):

#     model = Post
#     post_list = Post.objects.all()
#     category_list = Category.objects.all()
#     template_name = 'index.html'
