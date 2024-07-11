from django.shortcuts import render
from django.http import HttpResponse
 #METODLAR ASLINDA BİRER VİEW'DİR VE VİEW ALTINDA TUTULUR

# Create your views here.
#home metodu request isimli bir parametre alır ve aldığı request'e göre response olarak 'anasayfa' döndürür
def home(request):
    return HttpResponse('anasayfa')#httpResponse olarak anasayfa yazısını çağrılıdığı yerde döndürür.

#kullanıcıdan gelen request parametresini alır. request kullanıcıdan db'ye gönderilen istek kümesidir güvenlik açısından mutlaka kontrol edilmelidir
def courses(request):
    return HttpResponse('Kurs Listeleri')
