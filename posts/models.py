from django.db import models
# from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Data-model for post categories.
    """
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Data-model for posts added onto the site.
    """
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True, blank=False,
                             null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    vote_count = models.ManyToManyField(User, related_name='vote_count',
                                        blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Data-model for post comments.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=120)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
