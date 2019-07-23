from django.db import models

# Create your models here.
class Disney(models.Model):
    char_name=models.CharField(max_length=200)
    image_url=models.URLField(null=True)
    body=models.TextField(null=True)

class Name(models.Model):
    name=models.CharField(max_length=200)