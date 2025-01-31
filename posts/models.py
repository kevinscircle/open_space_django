from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts/images")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")



    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")



    def __str__(self):
        return f"{self.content}, {self.created_on}, {self.user}"