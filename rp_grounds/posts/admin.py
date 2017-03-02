from django.contrib import admin
from .models import Post
from .forms import BlogPost
# Register your models here.
admin.site.register(Post)