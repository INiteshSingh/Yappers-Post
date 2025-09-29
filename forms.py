from django import forms
from Blog.models import Blog_Data

class write_your_blog(forms.ModelForm):
    Blog_Author = forms.CharField(max_length=30)
    Blog_Title = forms.CharField(max_length=30)
    Blog_Content = forms.Textarea()
    Blog_Image = forms.ImageField()
    class Meta:
        model = Blog_Data
        fields = ["Blog_Author","Blog_Title","Blog_Content","Blog_Image"]
        

        
    