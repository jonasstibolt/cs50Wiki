from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test")
    # path("<str:entry_name>", views.entry, name="entry") #added this path
    ]
