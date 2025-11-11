 
from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('finc.urls')),
    path("c/",include("client.urls")),
]
