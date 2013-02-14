import mimetypes
import os

from PIL import Image as PILImage
from PIL import ImageOps

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.servers.basehttp import FileWrapper
from gal.models import Image
from gal import settings


def index(request):
    images = [image.filename for image in Image.objects.all()]
    return render_to_response('index.html', {'title': 'index',
                                             'images': images})


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

