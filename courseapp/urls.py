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
from django.contrib import admin
from django.http import HttpResponse #HttpResponse kütüphanesi django.http'den bu projeye import edildi
from django.urls import path, include




#route = http://127.0.0.1:8000/ bu url temsil eder
#view= pythonda kullandığımız method veya diğer adıyla iş yapan fonkisyonlar



#urlpatterns bir url şemasıdır ve metod ile burada url bağlanır
urlpatterns=[

    path('/',include('courses.urls')), #courses uygulamaısndaki urls.py içindeki urlspattern içini çağırıyor.include methodunu yukarıda import ettikten sonra burada kullanırız bu metod bize farlklı uygulama içinde tanımlanmış bilgileri farklı bir app içinde çağırabiliyorsun.
    path('admin/', admin.site.urls),
]
"""
Aslında burada yukarıda yaptığımız urlpatterns (url şeması)'nı ait olduğu uygulama içinden buraya yani ana uygulamaya çağırmalıyız burada tanımlamamalıyız 
mesela admin uygulaması başka bir yerde ve biz admin url ile request eşleştirmesini burada farklı bir yolla yapmalıyız.
"""