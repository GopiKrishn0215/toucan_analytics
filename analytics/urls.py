from django.urls import path
from .views import *

urlpatterns = [
    path('analytics',analytics),
    path('',index)
]