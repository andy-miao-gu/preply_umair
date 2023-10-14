from django.urls import path
# we need urls to see view, view is alreayd there in view.py
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("abc", views.index2, name="index2"),
]