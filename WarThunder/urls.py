from django.urls import path
from WarThunder import views

urlpatterns = [
    path('get/air', views.get_aircraft_information_api),
    path('get/air/<int:id>', views.get_aircraft_information_by_id_api),
    path('get/air/<str:name>', views.get_aircraft_information_by_name_api),
    path('post/air', views.post_aircraft_information_api),
    path('put/air/<int:id>', views.put_aircraft_information_api),
    path('delete/air/<int:id>', views.delete_aircraft_information_api),
]
