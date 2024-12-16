from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class myproject(models.Model):

    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=200)
    photo=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    
# Create your models here.
