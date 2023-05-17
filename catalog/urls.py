from django.urls import path
from catalog.apps import MainConfig
from catalog.views import index, contacts

app_name = MainConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
]