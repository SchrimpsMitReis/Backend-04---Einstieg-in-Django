from django.shortcuts import redirect
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.text import slugify
from django.urls import reverse
from .dummy_data import gadgets 
import json
# Create your views here.


def startPageView(request):
    return HttpResponse("Hey das hat ja doll funktioniert!!")

def singleGadgetIntView(request, gadget_id):
    new_slug = slugify(gadgets[gadget_id]['name'])
    new_url = reverse("gadget_slug_url", args=[new_slug])
    return redirect(new_url)

def singleGadgetsSlugView(request, gadget_slug=""):

    if request.method == "GET":
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget['name']) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das war was"})
        except:
            return JsonResponse({"response": "Das war wohl nix"})

