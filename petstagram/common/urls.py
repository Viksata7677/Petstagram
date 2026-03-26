from django.urls import path

from petstagram.common import views

urlpatterns = [
    path('', views.show_all_photos, name='homepage'),
    path('like/<int:photo_id>/', views.likes_functionality, name='like')
]