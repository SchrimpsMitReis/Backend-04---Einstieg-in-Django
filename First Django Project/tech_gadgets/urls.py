from django.urls import path
from .views import startPageView, singleGadgetsView, singleGadgetsSlugView, postView


urlpatterns = [
    path('', startPageView),
    path('gadget/<int:gadget_id>', singleGadgetsView),
    path('gadget/<slug:gadget_slug>', singleGadgetsSlugView , name="gadget_slug_url"),
    path('gadget/send_gadget/', postView)
]
