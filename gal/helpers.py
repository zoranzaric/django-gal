import os

from django.conf import settings

from gal.models import Image, Gallery

def get_galleries():
    return Gallery.objects.all().order_by('name')

def get_images_for_gallery(gallery_name):
    gallery = Gallery.objects.get(name=gallery_name)
    return gallery.image_set.all().order_by('filename')

def get_previous_image(gallery, image):
    images = get_images_for_gallery(gallery)
    last_image = None
    for i, img in enumerate(images):
        if img.filename == image.filename:
            return last_image
        last_image = img

def get_next_image(gallery, image):
    images = get_images_for_gallery(gallery)
    next = False
    for i, img in enumerate(images):
        if next:
            return img
        if img.filename == image.filename:
            next = True

