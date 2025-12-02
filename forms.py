from django import forms
from Blog.models import Blog_Data,User_Data
from django.contrib.auth.models import User

class login_Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password","email","first_name","last_name"]

class write_your_blog(forms.ModelForm):
    Blog_Author = forms.CharField(max_length=30)
    Blog_Title = forms.CharField(max_length=30)
    Blog_Content = forms.Textarea()
    Blog_Image = forms.ImageField()
    class Meta:
        model = Blog_Data
        fields = ["Blog_Author","Blog_Title","Blog_Content","Blog_Image"]

class user_data(forms.ModelForm):
    class Meta:
        model = User_Data
        fields = ['user_name','user_bio','profile_photo','joined_date']
