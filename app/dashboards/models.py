from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name
