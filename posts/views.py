from django.shortcuts import render
from django.views import View

# def home(request):
#     return render(request, 'base.html')


class Homepage(View):

    def get(self, request):
        return render(request, 'index.html')
