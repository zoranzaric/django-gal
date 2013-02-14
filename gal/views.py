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


def index(request):
    images = [image.filename for image in Image.objects.all().order_by('filename')]
    return render_to_response('index.html', {'title': 'index',
                                             'images': images})


def image(request, filename):
    image = get_object_or_404(Image, filename=filename)

    previous_image = get_previous_image(image)
    if previous_image:
        previous_image_filename = previous_image.filename
    else:
        previous_image_filename = ''

    next_image = get_next_image(image)
    if next_image:
        next_image_filename = next_image.filename
    else:
        next_image_filename = ''

    result = {
        'title': filename,
        'image': image.filename,
        'previous_image': previous_image_filename,
        'next_image': next_image_filename
    }

    return render_to_response('image.html', result)


def view_image(request, filename):
    image = get_object_or_404(Image, filename=filename)
    path = os.path.join(settings.GAL_IMAGES_DIR, image.filename)
    wrapper = FileWrapper(file(path))
    response = HttpResponse(wrapper,
                            content_type=mimetypes.guess_type(filename))
    response['Content-Length'] = os.path.getsize(path)
    return response

def view_thumbnail(request, filename):
    image = get_object_or_404(Image, filename=filename)
    path = os.path.join(settings.GAL_IMAGES_DIR, image.filename)
    pil_image = PILImage.open(path)

    thumb = ImageOps.fit(pil_image, (150, 150), PILImage.ANTIALIAS)

    response = HttpResponse(mimetype="image/png")
    thumb.save(response, "PNG")
    return response


def download_all(request):
    in_memory = StringIO()
    zip = ZipFile(in_memory, "a")
    for image in Image.objects.all():
      path = os.path.join(settings.GAL_IMAGES_DIR, image.filename)
      zip.write(path, image.filename)
    zip.close()

    response = HttpResponse(mimetype="application/zip")
    response["Content-Disposition"] = "attachment; filename=all.zip"
    response["Content-Length"] = in_memory.len
    in_memory.seek(0)
    response.write(in_memory.read())
    return response

