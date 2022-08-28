from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
