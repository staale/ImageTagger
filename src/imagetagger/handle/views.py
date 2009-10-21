from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from imagetagger.handle.models import ImageFile
from imagetagger.handle.models import ScannedImage

import Image
import os

def list_unhandled(request):
    ctx = {
        "image": ImageFile.objects.filter(scanned_image=None).order_by("-path")[0]
    }
    return render_to_response('list_unhandled.xhtml',
                              ctx,
                              context_instance=RequestContext(request))

def save_unhandled_image(request, image_id):
    image = get_object_or_404(ImageFile, pk=int(image_id))
    assert image.scanned_image is None, "Image is allready attached to a ScannedImage"%iamge.id
    assert ScannedImage.objects.filter(original=image).count() == 0, "There are allready ScannedImages using this image"

    scanned = ScannedImage(source=request.POST["source"], source_date=request.POST["source_date"], description=request.POST["description"], original=image)
    scanned.save()

    image.scanned_image = scanned
    image.save()
    return HttpResponseRedirect(reverse(list_unhandled))

def thumb(request, image_id):
    image = get_object_or_404(ImageFile, pk=int(image_id))
    image = Image.open(os.path.join(settings.OUTPUT_FOLDER, image.path))
    image.thumbnail((800,800))

    resp = HttpResponse(mimetype="image/jpeg")
    image.save(resp, format="jpeg")
    return resp

def full(request, image_id):
    image = get_object_or_404(ImageFile, pk=int(image_id))
    image = Image.open(os.path.join(settings.OUTPUT_FOLDER, image.path))

    resp = HttpResponse(mimetype="image/jpeg")
    image.save(resp, format="jpeg")
    return resp