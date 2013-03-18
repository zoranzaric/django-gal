from django.db import models

class Galery(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s" % self.name

class Image(models.Model):
    filename = models.CharField(max_length=255)
    gallery = models.ForeignKey(Galery)
    picked = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s/%s" % (self.gallery, self.filename)

