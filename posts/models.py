from django.db import models
from users.models import User


class Category(models.Model):
    """
    Data-model for post categories.
    """
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, null=False)

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
    vote_count = models.ManyToManyField(User, related_name='post_like',
                                        blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    """
    Data-model for post comments.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=120)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
