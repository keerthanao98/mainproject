from django.db import models

# Create your models here.


class Todo(models.Model):
    data = models.CharField(max_length=100)


