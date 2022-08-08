from django.db import models
from users.models import User


class Category(models.Model):
    """
    Data-model for post categories.
    """
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, null=False)


class Post(models.Model):
    """
    Data-model for posts added onto the site.
    """
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    vote_count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Data-model for post comments.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
