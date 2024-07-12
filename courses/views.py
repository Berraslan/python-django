
from django.shortcuts import render
from django.http import HttpResponse #açıklaması HttpResponse dosyasından http moteodlarını kulladır


def home(request):
    return HttpResponse('anasayfa')

def courses(request):
    return HttpResponse('kurs listesi')