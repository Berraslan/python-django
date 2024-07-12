from django.urls import path
from . import views  # views dosyasındaki her şeyi burada kullan

urlpatterns = [
    path('', views.courses), #herhangi bir parametre eklenmeden de courses view içine yönlendirebiliriz
    path('list', views.courses),  # http://127.0.0.1:8000/kurs/list
    path('<kurs_ad>', views.details),  # http://127.0.0.1:8000/kurs/details
    path('kategori/<int:category_id>',views.getCourseByCategoryId), #int ve str olarak ayırdık ki metodlar birbirine karışmasın ilgisi olmayan sayfalar birbiri altında gösterilmesin
    path('kategori/<str:category_name>',views.getCourseByCategoryName), # <değişkenAdi> yazılır ve dinamik url alınır #not dinamik url alma böyle yapılır ama dinamik url alırken dinamiği en sona yazarız statik olanlar başa yazılır yoksa değişkene uyarsa dinamik static olanı ezer

]
