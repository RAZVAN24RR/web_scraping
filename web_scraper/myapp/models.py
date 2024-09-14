from django.db import models

from django.db import models;

class Article(models.Model):
    title = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()

    def __str__(self):
        return self.title;

# Create your models here.
