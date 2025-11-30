from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup_page',views.signup_page,name="signup_page"),
    path('login_page',views.login_page,name ="login_page"),
    path('blog_form',views.blog_form,name="blog_form"),
    path('view_blog',views.view_blogs,name="view_blogs")
]


