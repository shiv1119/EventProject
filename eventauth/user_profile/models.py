from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, default='')
    last_name = models.CharField(max_length=300, default='')
    profile_image = models.ImageField(upload_to='profileImage/', blank=True, null=True)
    phone = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.first_name
    