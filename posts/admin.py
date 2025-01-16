from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_on', "user")

admin.site.register(Post, PostAdmin)