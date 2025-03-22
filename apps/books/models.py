from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
