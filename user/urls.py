from django.urls import path
from .views import Users, Update

urlpatterns = [
    path('register/', Users.as_view(name='register')),
    path('login/', Users.as_view(name='login')),
    path('logout/', Users.as_view(name='logout')),
    path('update/avatar/', Update.as_view(name='avatar')),
    path('update/info/', Update.as_view(name='info')),
    path('changepwd/', Update.as_view(name='pwd')),
]