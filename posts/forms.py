from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.TextInput()

    # def __init__(self, author):
    #     self.author = request.user.username
    #     super(PostForm, self).__init__()

    class Meta:
        model = Post
        fields = ('title', 'content', 'category')
