import mimetypes
import os

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

