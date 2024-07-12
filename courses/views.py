from django.http import HttpResponse


def courses(request):
    return HttpResponse('Kurs Listesi')


def details(request,kurs_ad):
    return HttpResponse(f'{kurs_ad} hakkında detaylar görüyorsunuz ')


#dinamik tanımlanmış url'in view yapısıdır ve request haricinde category adında <...> içine yazılan değeri yazar
def getCourseByCategoryName(request, category_name):
    text = ""
    if (category_name == "programlama"):
        text = "programlama kategorisine aittir"
    elif (category_name == "web-gelistirme"):
        text = "web geliştime kategorisine aittir"
    else:
        text = "yanlış kategori seçimi"
    return HttpResponse(f'{text}')

def getCourseByCategoryId(request, category_id):
    text=""
    if(category_id==1):
        text=f"{category_id} no'lu Kategroiyi görmektesiniz."
    elif(category_id==2):
        text=f"{category_id} no'lu Kategroiyi görmektesiniz."
    else:
        text = "Kategori dışı değer tespit edildi."

    return HttpResponse(text)#aldığı category_id'yie tekrar sayfaya basar.