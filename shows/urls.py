from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows_list, name="shows")
]