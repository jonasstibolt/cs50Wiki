from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new_page/', views.new_page, name='new_page'),
    path("randompage/", views.randompage, name="randompage"),
    path("test/", views.test, name="test"),
    path("search_results/", views.search_results, name="search_results"),
    path('edit/<str:title>/', views.edit_entry, name='edit_entry'),
    path("<str:title>", views.entry, name="entry")
    ]
