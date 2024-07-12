from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),  # parametresiz iken de home view return edilir
    path('iletisim/', views.iletisim),
    path('hakkimizda/', views.hakkimizda),
    path('anasayfa/', views.home),
    path('home/', views.home),
]
