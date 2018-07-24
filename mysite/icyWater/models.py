from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=50,default="")
    music=models.FileField(upload_to='isemusic',null=True)
    description =(models.TextField(max_length=100,default=""))
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
