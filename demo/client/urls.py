# kyc/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_kyc, name="kyc_upload"),
    path("<int:pk>/", views.kyc_detail, name="kyc_detail"),
    path("my/", views.my_kyc_list, name="kyc_list"),
]
