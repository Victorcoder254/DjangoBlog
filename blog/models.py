from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    introduction = models.TextField()
    intro_image = models.ImageField(upload_to='intro/')
    body_blog = models.TextField()
    image_body = models.ImageField(upload_to='body/')
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']
   

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'comments')
    body = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['date_posted']

