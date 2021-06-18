from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technology = models.CharField(max_length=40)
    image = models.FilePathField(path="/img")