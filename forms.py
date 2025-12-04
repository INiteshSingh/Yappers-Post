from django import forms
from Blog.models import Blog_Data
from django.contrib.auth.models import User

class login_Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password","email"]

class write_your_blog(forms.ModelForm):
    Blog_Title = forms.CharField(max_length=30)
    Blog_Author = forms.CharField(max_length=30)
    Blog_Content = forms.Textarea()
    Blog_Image = forms.ImageField()
    class Meta:
        model = Blog_Data
        fields = ["Blog_Title","Blog_Author","Blog_Content","Blog_Image"]
