from django.urls import path
from .views import startPageView, singleGadgetIntView, singleGadgetsSlugView


urlpatterns = [
    path('', startPageView),
    path('gadget/', singleGadgetsSlugView),
    path('gadget/<int:gadget_id>', singleGadgetIntView),
    path('gadget/<slug:gadget_slug>', singleGadgetsSlugView , name="gadget_slug_url"),
]
