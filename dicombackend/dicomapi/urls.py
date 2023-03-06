from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', upload),
    path('dicom/', dicom),
    path('volume/', volume),
]