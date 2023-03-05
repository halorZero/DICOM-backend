from django.urls import path
from .views import *

urlpatterns = [
    #path('upload/file', upload_file),
    path('dicom/', dicom),
    path('volume/', volume),
]