from django.shortcuts import render,redirect
from forms import write_your_blog,signupForm, login_Form
from .models import Blog_Data
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
# Create your views here.
def home(request):
    user = request.user
    # if request.user.is_authenticated:
    #     user_name = user.username
    #     # user_image = "media/profile_photos/default-female-profile-photo.jpg" if user.user_gender == "Female" else "media/profile_photos/default-male-profile-photo.jpg"
    #     if user.user_gender == "MALE":
    #         user_image = "media/blog_images/default-male-profile-photo.jpg"
    #     else:
    #         user_image = "media/blog_images/default-female-profile-photo.jpg"
    #     context = {
    #         "user_name":user_name,
    #         "user_image":user_image
    #     }
    #     return render(request,'Blog/Yappers Post.html',context)
    # else:
    return render(request,'Blog/Yappers Post.html')

def signup_page(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['user_password'])
            user.save()
            return redirect('login')
        else:
            error_message = "Invalid Data, Please Check Your Input"
            return render(request,'registration/signup_page.html',{
                "form":form,
                "error_message":error_message
            })
    else:
        form = signupForm()
    return render(request,'registration/signup_page.html',{"form":form}) 

def login_page(request):
    form = login_Form()
    if request.method == "POST":
        form = login_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Username or Password is Incorrect"
                return render(request,'registration/login.html',{'form':form,
                                                                'error_message':error_message})
    else:
        form = login_Form()      
        return render(request,'registration/login.html')

@login_required
def blog_form(request):
    form = write_your_blog()
    submit_status = False
    if request.method == "POST":
        form = write_your_blog(request.POST)
        submit_status = True
        if form.is_valid():
            form.save()
            print("Blog Saved")    
    return render(request,"Blog/blogform.html",{"form":form,"submit_status":submit_status})

@login_required
def view_blogs(request):
    current_blogs = Blog_Data.objects.all()
    return render(request,"Blog/viewblogs.html",{"current_blogs":current_blogs})