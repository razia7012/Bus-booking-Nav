from django.urls import path
from . import views

urlpatterns=[

        path('',views.home,name='base'),
        path('bus-list/',views.bus_list,name='bus-list'),
        path('search_buses/',views.search_buses,name='search'),


]