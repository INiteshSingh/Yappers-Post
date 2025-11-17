from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('blog_form',views.blog_form,name="blog_form"),
    path('view_blog',views.view_blogs,name="view_blogs")
]


