from django.db import models

# Create your models here.
class Blog_Data(models.Model):
    Blog_Author = models.CharField(max_length=30)
    Blog_Title = models.CharField(max_length=30)
    Blog_Content = models.TextField()
    