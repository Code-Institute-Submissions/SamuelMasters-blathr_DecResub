from django import forms
# from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Class for Posts
    """
    title = forms.CharField(max_length=100)
    content = forms.TextInput()

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')


class CommentForm(forms.ModelForm):
    """
    Class for Comments
    """
    class Meta:
        model = Comment
        fields = ('body',)
