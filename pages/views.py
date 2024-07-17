from django.http import HttpResponse
from django.shortcuts import render

#render metdou bir html sayfası döndürür ve mutlaka parametre olarak request alır ikinci olarak template_name alır parametre olarak render ama dikkat str olarak alır
def index(request):
    return render(request,'pages/index.html') #render aracılığı ile tempalates klasörü içindeki index.html sayfası çağrılır.index html ilk olarak hangi uygulmaa iiçinde çağrıldıysa o uygulama içindeki tanımlandığı yerde aranır
def contact(request):
    return render(request,'pages/contact.html')
def about(request):
    return render(request,'pages/about.html')

