from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage/", views.newpage, name="newpage"),
    path("randompage/", views.randompage, name="randompage"),
    path("test/", views.test, name="test"),
    path("search_results/", views.search_results, name="search_results"),
    path("<str:title>", views.entry, name="entry") #added this path
    ]
