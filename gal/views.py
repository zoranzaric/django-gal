import mimetypes
import os

from StringIO import StringIO
from zipfile import ZipFile

from PIL import Image as PILImage
from PIL import ImageOps

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.servers.basehttp import FileWrapper
from gal.models import Image
from gal import settings
from gal.helpers import *


def index(request, gallery):
    images = [image.filename for image in get_images_for_gallery(gallery)]
    return render_to_response('index.html', {'title': 'index',
                                             'gallery': gallery,
                                             'images': images})


def image(request, gallery, filename):
    image = get_object_or_404(Image, filename=filename)

    previous_image = get_previous_image(gallery, image)
    if previous_image:
        previous_image_filename = previous_image.filename
    else:
        previous_image_filename = ''

    next_image = get_next_image(gallery, image)
    if next_image:
        next_image_filename = next_image.filename
    else:
        next_image_filename = ''

    result = {
        'gallery': gallery,
        'title': filename,
        'image': image.filename,
        'previous_image': previous_image_filename,
        'next_image': next_image_filename
    }

    return render_to_response('image.html', result)


def view_image(request, gallery, filename):
    image = get_object_or_404(Image, filename=filename)
    path = os.path.join(settings.GAL_IMAGES_DIR, gallery, image.filename)
    wrapper = FileWrapper(file(path))
    response = HttpResponse(wrapper,
                            content_type=mimetypes.guess_type(filename))
    response['Content-Length'] = os.path.getsize(path)
    return response

def view_thumbnail(request, gallery, filename):
    size = (150, 150)

    image = get_object_or_404(Image, filename=filename)

    prefix = "thumb_%d_%d_" % size
    if not os.path.exists(os.path.join(settings.GAL_IMAGES_CACHE_DIR, gallery)):
        os.mkdir(os.path.join(settings.GAL_IMAGES_CACHE_DIR, gallery))
    cache_path = os.path.join(settings.GAL_IMAGES_CACHE_DIR, gallery, prefix + image.filename)
    if not os.path.exists(cache_path):
        path = os.path.join(settings.GAL_IMAGES_DIR, gallery, image.filename)
        pil_image = PILImage.open(path)

        thumb = ImageOps.fit(pil_image, size, PILImage.ANTIALIAS)
        thumb.save(cache_path)
    else:
        thumb = PILImage.open(cache_path)

    response = HttpResponse(mimetype="image/png")
    thumb.save(response, "PNG")
    return response


def download_all(request, gallery):
    in_memory = StringIO()
    zip = ZipFile(in_memory, "a")
    for image in get_images_for_gallery(gallery):
      path = os.path.join(settings.GAL_IMAGES_DIR, image.filename)
      zip.write(path, image.filename)
    zip.close()

    response = HttpResponse(mimetype="application/zip")
    response["Content-Disposition"] = "attachment; filename=all.zip"
    response["Content-Length"] = in_memory.len
    in_memory.seek(0)
    response.write(in_memory.read())
    return response

