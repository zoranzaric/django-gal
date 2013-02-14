from django.db import models

class Image(models.Model):
    filename = models.CharField(max_length=255)

