from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
from django.views.generic.base import RedirectView
from .dummy_data import gadgets
import json
# Create your views here.


def startPageView(request):
    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})


def singleGadgetIntView(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]['name'])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found by me")


class GadgetView(View):

    def get(self, request, gadget_slug=""):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget['name']) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    def post(self, request):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das war was"})
        except:
            return JsonResponse({"response": "Das war wohl nix"})


class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"
    # print("Hello")
    def get_redirect_url(self, *args, **kwargs):
        new_slug = slugify(gadgets[kwargs.get('gadget_id', 0)]['name'])
        new_kwarg = {"gadget_slug" : new_slug}
        return super().get_redirect_url(*args, **new_kwarg)

# def singleGadgetsSlugView(request, gadget_slug=""):

#     if request.method == "GET":
#         gadget_match = None
#         for gadget in gadgets:
#             if slugify(gadget['name']) == gadget_slug:
#                 gadget_match = gadget

#         if gadget_match:
#             return JsonResponse(gadget_match)
#         raise Http404()
    
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             print(f"recieved data: {data}")
#             return JsonResponse({"response": "Das war was"})
#         except:
#             return JsonResponse({"response": "Das war wohl nix"})

