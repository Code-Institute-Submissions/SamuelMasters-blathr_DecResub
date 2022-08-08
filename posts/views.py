from django.shortcuts import render, HttpResponse

def test_func(request):
    return HttpResponse("Testing...")
