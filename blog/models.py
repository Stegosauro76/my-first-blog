# blog/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):

    title = models.CharField(max_length=200)

    body = models.TextField()  

    created_at = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):

    author = models.CharField(max_length=60)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey("Post", on_delete=models.CASCADE)
