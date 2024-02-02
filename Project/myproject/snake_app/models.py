from django.db import models
from django.utils import timezone

# Create your models here.
class user(models.Model):
    Username=models.CharField(max_length=20)
    u_id=models.IntegerField(primary_key=True,default=0)
    Name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)

class snake(models.Model):
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.image.name
    

class DeepLearningModel(models.Model):
    architecture = models.TextField()
    weights = models.FileField(upload_to='models/')
    
    
