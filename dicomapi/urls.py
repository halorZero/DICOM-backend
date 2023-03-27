from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload),
    path('dicom/', dicom),
    path('dicom2/', dicom2),
    path('dicom3/', dicom3),
    path('dicom4/', dicom4),
    path('dcmlength/', dicom4length),
    path('volume/', volume),
]