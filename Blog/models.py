from django.db import models
from datetime import date
# Create your models here.

class User_Data(models.Model):
    class Gender(models.TextChoices):
        MALE = "M","Male",
        FEMALE = "F","Female",
        OTHER = "O","Other"

    first_name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=30,null=False)
    yapp_username = models.CharField(max_length=30,unique=True,null=False)
    user_password = models.CharField(max_length=30,null=False)
    user_bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile_photos/',blank=True,null=True,default="profile_photos/default-male-profile-photo.jpg")
    joined_date = models.DateField(default=date.today)
    user_gender = models.CharField(
        max_length=1,
        choices = Gender.choices,
        default=Gender.MALE,
        null=False,)

class Blog_Data(models.Model):
    Blog_Author = models.CharField(max_length=30)
    Blog_Title = models.CharField(max_length=30)
    Blog_Content = models.TextField()
    Blog_Image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
    Created_At = models.DateField(auto_now=True)
