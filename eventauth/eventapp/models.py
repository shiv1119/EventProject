from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=300)
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    time = models.TimeField()
    location = models.CharField(max_length=300)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    specification = models.CharField(max_length=2000)
    outcomes = models.CharField(max_length=1000)
    is_liked = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.event_name
    

