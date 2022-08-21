from .models import Post
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.TextInput()

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')
