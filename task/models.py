from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=1000)
    report = models.TextField(max_length=5000)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    service_name = models.CharField(max_length=100)
    status = models.BooleanField()



class Category(models.Model):
    name = models.CharField(max_length=100)