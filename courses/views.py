from datetime import date
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse  #django altındaki urls kütüphanesinden reverse metodunu import ettik projeye


#404 eror - kullanıcının yanlış bir request de bulunduğunu gösterir
#200 - başarılı request ve respons alındı
#201 - veritababnında değişikliğe neden olan status kodu
#500'lü hatalar -server kaynaklı hatalar
 #not neden index.html sayfasını tempaletes klasörü altında yeniden bir courses directory oluşturup oraya koyduk çünkü eper farklı uygulamamlar içinde aynı .html adlı html sayfası varsa eğer o uygulammada bulamazsa öbür uygulmamadaki html sayfasını çağırırı ama biz templates içine yeni bir director koyarak aslında html dosuyası önüne director pages/index.html koyuyoruz böylelikle sadece o pages klasörü altında html sayfasını arıyıp çağırmasını sağlıyoruz

data = {
    "programlama": "programlama kategorsine ait kurslar",
    "web-geliştireme": "web geliştirme kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar",
    "mobil-uygulama": "mobil kategorisine ait kurslar",

}

db={
    "courses": [
        {
            "title":"javascript kursu",
            "description": "javascript kurs açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug":"javascript-kursu",
            "date":date(2022,10,10),
            "is-active":True

        },
        {
            "title":"python kursu",
            "description": "pyhton kurs açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug":"pyhton-kursu",
            "date":date(2022,9,10),
            "is-active":False
        },
        {
            "title":"web geliştirme kursu",
            "description": "web geliştirme kurs açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug":"web-geliştirme-kursu",
            "date":date(2022,8,10),
            "is-active":True
        },
    ], 'categories':["programlama kategorisi","web geliştirme kategorisi","mobil geliştirme kategorisi"]
}


def index(request):
    list_items=""
    category_list=list(data.keys())
    return render(request ,'courses/index.html',{
        'categories' : category_list
    })




#request : http://127.0.0.1:8000/ tutar kurs_ad urls.py'deki details urlspatterns içindeki kullanıcını <kurs_ad> değişkeni içine girdiği değeri tutar.
def details(request, kurs_ad):
    return HttpResponse(f'{kurs_ad} hakkında detaylar görüyorsunuz')



#dinamik tanımlanmış url'in view yapısıdır ve request haricinde category adında <...> içine yazılan değeri yazar kısaca request :http://127.0.0.1:8000/ statik yapıyı tutar category_name : kullanıcının yazdığı dinamik değeri tutar
def getCourseByCategoryName(request, category_name):
    try:
        category_text = data[category_name]
        return render(request,'courses/courses.html',{
            'category': category_name,
            'category_text': category_text
        })

    except:
        return HttpResponseNotFound("yanlış kategori seçimi")


def getCourseByCategoryId(request, category_id):
    category_list = list(data.keys())  #data listesi içindeki tüm keysler listeye çevrilip category_list içine atılır.
    if (category_id > len(
            category_list)):  #eğerki kullanıcının girdiği id bilgisi elimizde mevcut olan keys eleman saysından fazla ise bu bir hatatdır elimizde olmayan bir kurs talep ediliyor hata döndürürüz
        return HttpResponseNotFound("<h1>yanlış kategori seçimi</h1>")
    category_name= category_list[category_id - 1]  #kullanıcından gelen id numarasının bir eksiği alınır ki listede indis 0'dan başladığı için kullanıcının girdiği sayının bir eksiği alınır yani 1 no'lu elemana erişmesi için aslında 0. indise erişmeli

    redirect_url = reverse('courses_by_category',args=[category_name]) # urli yani kurs/kategori/değişkenAdi urlini artık courses_by_category tutuyor değişkenAdini da category_name tutuyor

    return redirect(redirect_url) #burada getVourseByCategoryName view'ina yönledirme yapar
