from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
