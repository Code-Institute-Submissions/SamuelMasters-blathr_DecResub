from .models import Post
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.TextInput()

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['User'] = request.user

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')
