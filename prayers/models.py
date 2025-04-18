from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    prayer = models.TextField()

class Comment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=64, default="")
    body = models.TextField()


