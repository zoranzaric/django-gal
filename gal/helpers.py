from gal.models import Image

def get_previous_image(image):
    images = Image.objects.all().order_by('filename')
    last_image = None
    for i, img in enumerate(images):
        if img.filename == image.filename:
            return last_image
        last_image = img

def get_next_image(image):
    images = Image.objects.all().order_by('filename')
    next = False
    for i, img in enumerate(images):
        if next:
            return img
        if img.filename == image.filename:
            next = True

