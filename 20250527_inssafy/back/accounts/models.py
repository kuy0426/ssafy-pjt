from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    biography = models.CharField(max_length=200, blank=True, help_text="bio")
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, help_text="profile")
