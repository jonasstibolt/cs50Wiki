from django.urls import path

from . import views
from views import page #added this import

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.entry, name=f"{page}") #added this path
    ]
