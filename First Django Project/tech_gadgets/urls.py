from django.urls import path
from .views import ManufView, RedirectToGadgetView, singleGadgetIntView, GadgetView, singleManufIntView, startPageView


urlpatterns = [
    path('start/', startPageView, name="startpage"),
    path('', startPageView),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', singleGadgetIntView),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view() , name="gadget_slug_url"),
    path('manuf/', ManufView.as_view()),
    path('manuf/<int:manuf_id>', singleManufIntView),
    path('manuf/<slug:manuf_slug>', ManufView.as_view(), name="manuf_slug_url")
]



# Startseite um auf Gadgets oder Manifacturers umzuleiten
# '' ist als opf ad nicht aussagekräftig
# '' -> to Startpage
# Startpage: lists[gadgets, manufacturers]

# 'gadget/...' bleibt wie es ist. 
# 'manufacturers/.. wird ähnlich implimentiert