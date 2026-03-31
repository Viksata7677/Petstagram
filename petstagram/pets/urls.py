from django.urls import path, include

from petstagram.pets import views
from petstagram.pets.views import PetAddView, PetDetailsPage, PetEditView, PetDeletePage

urlpatterns = [
    path('add/', PetAddView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', PetDetailsPage.as_view(), name='pet-details'),
        path('edit/', PetEditView.as_view(), name='pet-edit'),
        path('delete/', PetDeletePage.as_view(), name='pet-delete')
    ]))
]