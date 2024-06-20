from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"), #Define a URL para a view home
]