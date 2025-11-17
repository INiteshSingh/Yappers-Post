from django.shortcuts import render,redirect
from forms import write_your_blog
from .models import Blog_Data
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'Blog/Yappers Post.html')

def signup_view(request):
    if request.method == "POST":
        form = form.signupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = signupForm()
    return render(request,'registration/signupPage.html') 

def login_view(request):
    if request.method == "POST":
        form = form.loginForm(request.POST)
        if form.is_valid():
            return redirect('welcomePage')
        else:
            pass
    else:
        form = loginForm()
    return render(request,'registration/loginpage.html')
@login_required
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

@login_required
def view_blogs(request):
    current_blogs = Blog_Data.objects.all()
    return render(request,"Blog/viewblogs.html",{"current_blogs":current_blogs})