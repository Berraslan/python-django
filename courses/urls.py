from django.urls import path
from . import views #açıklaması views dosysındaki tüm herşeyi burada kullanıdr

urlpatterns = [
    path('', views.home),  # parametresiz iken de home view return edilir
    path('kurslar/', views.courses),
    path('anasayfa/', views.home),
    path('home/', views.home),
]

