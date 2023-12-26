from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='image/professor')
    slug = models.CharField(max_length=40, unique=True,)
    occupation = models.CharField(max_length=50)
    description = models.TextField()