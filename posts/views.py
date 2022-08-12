from django.shortcuts import render
from django.views import View, generic
from .models import Post

# def home(request):
#     return render(request, 'base.html')


# class Homepage(View):

#     model = Post
#     queryset = Post.objects

#     def get(self, request):
#         return render(request, 'index.html')


class Homepage(generic.ListView):

    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
