from django.urls import path
from .views import RedirectToGadgetView, singleGadgetIntView, GadgetView, startPageView


urlpatterns = [
    path('start/', startPageView),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', singleGadgetIntView),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view() , name="gadget_slug_url"),
]
