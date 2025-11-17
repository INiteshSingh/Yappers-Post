from django import forms
from Blog.models import Blog_Data
from django.contrib.auth.models import User

class loginForm(forms.ModelForm):
    class Meta:
        model = 

class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["UserName","Password"]

class write_your_blog(forms.ModelForm):
    Blog_Author = forms.CharField(max_length=30)
    Blog_Title = forms.CharField(max_length=30)
    Blog_Content = forms.Textarea()
    Blog_Image = forms.ImageField()
    class Meta:
        model = Blog_Data
        fields = ["Blog_Author","Blog_Title","Blog_Content","Blog_Image"]
        

        

