from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/profile_image")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
