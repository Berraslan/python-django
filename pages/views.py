from django.http import HttpResponse


# Create your views here.
def iletisim(request):
    return HttpResponse('İletişim Sayfası')
def hakkimizda(request):
    return HttpResponse('Hakkımızda sayfasıdır')
def home(request):
    return HttpResponse('Ana sayfa')
