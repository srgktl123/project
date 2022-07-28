from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('login/', signin),
    path('logout/', log_out),
    path('signup/', signup),
]
