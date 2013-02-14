from gal.models import Image

def get_images_for_gallery(gallery):
    return Image.objects.filter(gallery__exact=gallery).order_by('filename')

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

