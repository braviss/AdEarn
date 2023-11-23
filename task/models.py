from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=1000)
    report = models.TextField(max_length=5000)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    service_name = models.CharField(max_length=100)
    status = models.BooleanField()
    slug = models.SlugField(default="", null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.DateTimeField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.created_at
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


