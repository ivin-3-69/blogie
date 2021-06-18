from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    user_name = models.CharField(max_length=40)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=40)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title