from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    """
    Data-model for user profiles registered on the site.
    """
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
