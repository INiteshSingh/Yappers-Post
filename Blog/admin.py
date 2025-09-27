from django.contrib import admin
from Blog.models import Blog_Data
# Register your models here.
class Blog_Admin(admin.ModelAdmin):
    list_display = ["Blog_Author","Blog_Title","Blog_Content"]

admin.site.register(Blog_Data,Blog_Admin)
