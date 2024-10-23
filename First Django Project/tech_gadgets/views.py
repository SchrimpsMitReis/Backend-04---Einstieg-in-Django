from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.utils.text import slugify
from django.urls import reverse
from .dummy_data import gadgets 
import json
# Create your views here.


def startPageView(request):
    return HttpResponse("Hey das hat ja doll funktioniert!!")

def singleGadgetsView(request, gadget_id):
    new_slug = slugify(gadgets[gadget_id]['name'])
    new_url = reverse("gadget_slug_url", args=[new_slug])
    return redirect(new_url)

def singleGadgetsSlugView(request, gadget_slug):
    gadget_match = {'result' : 'nixe'}
    for gadget in gadgets:
        if slugify(gadget['name']) == gadget_slug:
            gadget_match = gadget

    return JsonResponse(gadget_match)

def postView(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das war was"})
        except:
            return JsonResponse({"response": "Das war wohl nix"})