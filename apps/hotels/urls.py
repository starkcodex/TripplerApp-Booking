from django.contrib import admin
from django.urls import path, include
from  .views import hotelview, add_hotel

urlpatterns = [
    path('', hotelview , name='hotel'),
    path('add/', add_hotel , name='add-hotel')
]
