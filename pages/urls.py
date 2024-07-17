from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),  #views dosyası altında index view'ı çağrılır
    path('contact/', views.contact),
    path('about/', views.about),
    path('index/', views.index),
]
