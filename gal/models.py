from django.db import models
from django.core.urlresolvers import reverse

class Gallery(models.Model):
    name = models.CharField(max_length=255, unique=True, default="")

    def __unicode__(self):
        return "%s" % self.name

class Image(models.Model):
    filename = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery, null=True)
    picked = models.BooleanField(default=False)

    @property
    def image_url(self):
        return reverse('gal.views.view_image',
                       args=[self.gallery.name, self.filename])

    def __unicode__(self):
        return "%s/%s" % (self.gallery, self.filename)

