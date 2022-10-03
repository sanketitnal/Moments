from django.db import models
import uuid
from datetime import date
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


def unique_file_name(instance, filename):
    file_ext = filename.split('.')[-1]
    return f'{date.today()}/{uuid.uuid4()}.{file_ext}'


class Picture(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=unique_file_name)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.title}:{self.picture.name}"
