from django.db import models

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    age = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
