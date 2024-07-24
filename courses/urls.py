from django.urls import path
from . import views  # views dosyasındaki her şeyi burada kullan

urlpatterns = [
    path('', views.index), #herhangi bir parametre eklenmeden de courses view içine yönlendirebiliriz
    path('<kurs_ad>', views.details),  # http://127.0.0.1:8000/kurs/details
    path('kategori/<int:category_id>',views.getCourseByCategoryId), #int ve str olarak ayırdık ki metodlar birbirine karışmasın ilgisi olmayan sayfalar birbiri altında gösterilmesin
    path('kategori/<str:category_name>',views.getCourseByCategoryName,name='courses_by_category'), #name ile bu url pattern'ine isim verdik kurslar/kategori ismini artık name tutuyor
]
