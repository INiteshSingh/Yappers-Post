from django.shortcuts import render
from forms import write_your_blog
from .models import Blog_Data
# Create your views here.
def home(request):
    return render(request,'Blog/Yappers Post.html')

def blog_form(request):
    form = write_your_blog()
    submit_status = False
    if request.method == "POST":
        form = write_your_blog(request.POST, request.FILES)
        submit_status = True
        if form.is_valid():
            form.save()
            print("Blog Saved")    
            
    return render(request,"Blog/blogform.html",{"form":form,"submit_status":submit_status})

def view_blogs(request):
    current_blogs = Blog_Data.objects.all()
    return render(request,"Blog/viewblogs.html",{"current_blogs":current_blogs})
