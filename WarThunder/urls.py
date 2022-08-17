from django.urls import path
from WarThunder import views

urlpatterns = [
    path('air', views.aircraft_information_api),
    path('air/<int:id>', views.aircraft_information_api),
    path('air/<str:name>', views.aircraft_information_api)
]
