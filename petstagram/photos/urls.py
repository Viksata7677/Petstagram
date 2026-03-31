from django.urls import path, include

from petstagram.photos import views
from petstagram.photos.views import PhotoAddPage, PhotoEditPage

urlpatterns = [
    path('add/', PhotoAddPage.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', PhotoEditPage.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete')
    ]))
]