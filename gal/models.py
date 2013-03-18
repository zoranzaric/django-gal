from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=255, unique=True, default="")

class Image(models.Model):
    filename = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery, null=True)
    picked = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s/%s" % (self.gallery, self.filename)

