from django.db import models

class Image(models.Model):
    filename = models.CharField(max_length=255)
    gallery = models.CharField(max_length=255, default="")
    picked = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s/%s" % (self.gallery, self.filename)

