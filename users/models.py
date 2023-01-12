from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to="pictures", default="avatar.webp")
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"