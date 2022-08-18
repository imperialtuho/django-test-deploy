from django.urls import path
from WarThunder import views

vehicle = 'vehicle'

urlpatterns = [
    path('home', views.index),
    path(f'get/{vehicle}/air', views.get_aircraft_information_api),
    path(f'get/{vehicle}/air/<int:id>',
         views.get_aircraft_information_by_id_api),
    path(f'get/{vehicle}/air/<str:name>',
         views.get_aircraft_information_by_name_api),
    path(f'post/{vehicle}/air', views.post_aircraft_information_api),
    path(f'put/{vehicle}/air/<int:id>', views.put_aircraft_information_api),
    path(f'delete/{vehicle}/air/<int:id>',
         views.delete_aircraft_information_api),
]
