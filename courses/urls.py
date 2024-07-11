from django.urls import path
#bu tanımlama aynı dizinde olan iki .py uzantılı dosya biribirne erişmesi için import edilme yöntemidir.
from courseapp.courses import views

#bu adresin sonuna parametreler ekleyeke örn : admin vs anasayfa gibi ve bu parametreleri gerekli kaynaklarla ilişkilendireceğiz
#http://127.0.0.1:8000/ => anasayfa'ya yönlendirecek
#http://127.0.0.1:8000/home => anasayfa'ya yönlendirecek
#http://127.0.0.1:8000/courses => kurs listesi sayfasına yönlendirecek


#url devamına anasayfa yazılırsa veya home veya kursalr yazılırsa views altındaki courses meeodu veya home metodu hngisi ilgili ise o çalışır.
urlpatterns = [
    path('', views.home),
    path('anasayfa', views.home),
    path('home', views.home),
    path('kurslar', views.courses),
]
