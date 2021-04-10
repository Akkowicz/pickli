from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add = True)
    content= models.TextField()