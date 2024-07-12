

""" http://127.0.0.1:8000/     = kullanıcı browser'a böyle yazarsa anasayfa çıksın diyip view içinde tanımlayabilirim
    http://127.0.0.1:8000/home = kullanıcı browser'a böyle yazarsa anasayfa çıksın diyip view içinde tanımlayabilirim
    http://127.0.0.1:8000/courses = kullanıcı browser'a böyle yazarsa kurs listesi çıksın diyip view içinde tanımlayabilirim.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),  # boş parametresiz geldiğinde pages sayfasındaki urls'lere erişiebilir şekilde yönlendir.
    path('kurs/', include('courses.urls')), #http://127.0.0.1:8000/kurs altındaki urllere gitsin demek
    path('admin/', admin.site.urls),#admin ön eki gelmişse admin'e gider
]

""" 

kodun açıklaması : urlpatterns içine path eklenir path('',home), gibi ve bunun anlamı  http://127.0.0.1:8000/ şeklinde boş parametresiz gelirse home view olarak tanımlanmış methoda git ve
def home(request):
    return HttpResponse('anasayfa') httpResponse ile aasayfa yazısını ekrana return et.
    
"""

#route = http://127.0.0.1:8000/ bu url temsil eder bu url sonuna eklenen parametreleri bağlamak istediğimiz sayfaya yönlendircez bu yönlendirme işlmeini ise view dosyası içinde metodlsr tanımlayıp url dosyasında çağırırız
#view= pythonda kullandığımız method veya diğer adıyla iş yapan fonkisyonlar


"""
Aslında burada yukarıda yaptığımız urlpatterns (url şeması)'nı ait olduğu uygulama içinden buraya yani ana uygulamaya çağırmalıyız burada tanımlamamalıyız 
mesela admin uygulaması başka bir yerde ve biz admin url ile request eşleştirmesini burada farklı bir yolla yapmalıyız.
"""
