from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    title = forms.TextInput()
    content = forms.TextInput()
    author = current_user
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'author')
