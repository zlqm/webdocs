from django.urls import path, re_path

from . import views

urlpatterns = [
    path('pets', views.PetsView.as_view()),
    path('pets/<int:pet_id>', views.PetView.as_view()),
    re_path(r'pets/(?P<pet_id>\d+)/images', views.PetImageView.as_view()),
]
