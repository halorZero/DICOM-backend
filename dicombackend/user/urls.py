from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Users.as_view(mode=0)),
    path('register/', Users.as_view(mode=1)),
]