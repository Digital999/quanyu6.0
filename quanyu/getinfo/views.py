from rest_framework.views import APIView
from rest_framework import status
from datastyle_change import get_data
from django.http import JsonResponse,HttpResponse
from change_to_pinyin import word
from .models import EveryComponent
class get_hotel(APIView):
    def post(self,request):
        if request.method=='POST':
            dizhi=request.data['dizhi']
            pinyin=word(dizhi)
            sql="SELECT hotel_name,location,pinfen,customer,price,images,city FROM hotelinfo_hotelinfo where city='%s'"%(pinyin)
            data=get_data(sql)
            return JsonResponse(data=data,safe=False)
class get_xiuxian(APIView):
    def post(self,request):
        if request.method=='POST':
            dizhi=request.data['dizhi']
            sql="SELECT * FROM getinfo_xiuxianyule where city='%s'"%(dizhi)
            data=get_data(sql)
            return JsonResponse(data=data,safe=False)
class get_nongjia(APIView):
    def post(self,request):
        if request.method=='POST':
            dizhi=request.data['dizhi']
            sql="SELECT * FROM getinfo_xiuxiannongjia where city='%s'"%(dizhi)
            data=get_data(sql)
            return JsonResponse(data=data,safe=False)
class Sumbmmit_hotel_Component(APIView):
    def post(self,request):
        if request.method=='POST':
           hotel_name=request.POST.get('hotel_name','')
           openid=request.POST.get('openid','')
           username=request.POST.get('username','')
           touxiang=request.POST.get('touxiang','')
           content=request.POST.get('content','')
           index=EveryComponent.objects.create(hotel_name=hotel_name,openid=openid,username=username,touxiang=touxiang,
                                               content=content)
        return HttpResponse(status=status.HTTP_201_CREATED)
class Sumbmmit_user_Component(APIView):
    def post(self,request):
        if request.method == 'POST':
           hotel_name=request.POST.get('hotel_name','')
           openid=request.POST.get('openid','')
           username=request.POST.get('username','')
           touxiang=request.POST.get('touxiang','')
           target=request.POST.get('target','')
           content=request.POST.get('content','')
           sql = "Select comment_amount FROM getinfo_everycomponent where id='%s'" % (target)
           data = get_data(sql)
           datas=data[0]['comment_amount']
           comment_amount_update=EveryComponent.objects.get(id=target)
           comment_amount_update.comment_amount=str(int(datas)+1)
           comment_amount_update.save()
           EveryComponent.objects.create(hotel_name=hotel_name,openid=openid,username=username,touxiang=touxiang,
                                               content=content,target=target)
        return HttpResponse(status=status.HTTP_201_CREATED)
class Get_hotel_Component(APIView):
    def post(self,request):
        if request.method=='POST':
            hotel_name=request.POST.get('hotel_name','')
            target='0'
            sql="Select * FROM getinfo_everycomponent where hotel_name='%s'and target='%s'order by time "%(hotel_name,target)
            data=get_data(sql)
            return JsonResponse(data=data,safe=False)
class Get_user_Component(APIView):
    def post(self,request):
        if request.method=='POST':
            target=request.POST.get('target','')
            sql="Select * FROM getinfo_everycomponent where target='%s'"%(target)
            data=get_data(sql)
            return JsonResponse(data=data,safe=False)