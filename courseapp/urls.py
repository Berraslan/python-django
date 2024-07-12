"""courseapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

""" http://127.0.0.1:8000/     = kullanıcı browser'a böyle yazarsa anasayfa çıksın diyip view içinde tanımlayabilirim
    http://127.0.0.1:8000/home = kullanıcı browser'a böyle yazarsa anasayfa çıksın diyip view içinde tanımlayabilirim
    http://127.0.0.1:8000/courses = kullanıcı browser'a böyle yazarsa kurs listesi çıksın diyip view içinde tanımlayabilirim.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('courses.urls')),  # courses`uygulamasının urls.py dosyasını dahil edin
    path('admin/', admin.site.urls),
]

"""kodun açıklaması : urlpatterns içine path eklenir path('',home), gibi ve bunun anlamı  http://127.0.0.1:8000/ şeklinde boş parametresiz gelirse home view olarak tanımlanmış methoda git ve
def home(request):
    return HttpResponse('anasayfa') httpResponse ile aasayfa yazısını ekrana return et.
"""

#route = http://127.0.0.1:8000/ bu url temsil eder bu url sonuna eklenen parametreleri bağlamak istediğimiz sayfaya yönlendircez bu yönlendirme işlmeini ise view dosyası içinde metodlsr tanımlayıp url dosyasında çağırırız
#view= pythonda kullandığımız method veya diğer adıyla iş yapan fonkisyonlar


"""
Aslında burada yukarıda yaptığımız urlpatterns (url şeması)'nı ait olduğu uygulama içinden buraya yani ana uygulamaya çağırmalıyız burada tanımlamamalıyız 
mesela admin uygulaması başka bir yerde ve biz admin url ile request eşleştirmesini burada farklı bir yolla yapmalıyız.
"""
