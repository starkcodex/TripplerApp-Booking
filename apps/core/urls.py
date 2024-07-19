from django.contrib import admin
from django.urls import path, include
from  .views import homepage, our_story


urlpatterns = [
    path('', homepage , name='homepage'),
    path('ourstory/', our_story , name='our-story'),
]
