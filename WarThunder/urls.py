from django.urls import path, re_path
from WarThunder import views

urlpatterns = [
    re_path(r'^air$', views.aircraft_information_api),
    re_path(r'^air/([0-9]+)$', views.aircraft_information_api)
]
