from .models import submmit,good,PicTest
from user.models import userinfo
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from datastyle_change import get_data
import redis
class Submmit(APIView):
    def post(self, request):
        if request.method == 'POST':
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            author = request.POST.get('author', '')
            photo=request.POST.get('photo','')
            data = userinfo.objects.get(openid=author).username
            touxiang=userinfo.objects.get(openid=author).images
            city=request.POST.get('city','')
            if data:
                submmit.objects.create(title=title,content=content,author_id=author,photo=photo,author_name=data,touxiang=touxiang,city=city)
                return HttpResponse(status=status.HTTP_201_CREATED)
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
class Common_list(APIView):
    def post(self,request):
        if request.method =='POST':
            city = request.POST.get('city', '')
            sql = "SELECT title,content,author_name,touxiang,photo,gooded,requests_math FROM share_submmit where is_pass='1'and city='%s'order by time " % (
                city)
            data = get_data(sql)
            return JsonResponse(data=data,safe=False)
        else:
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
class Singleshare(APIView):
    def post(self,request):
        if request.method=='POST':
            openid=request.POST.get('openid','')
            article_id=request.POST.get('article_id','')
            goods = good.objects.filter(author_id=openid, article_id=article_id)
            sql="SELECT requests_math FROM share_submmit where article_id='%s'"%(article_id)
            data=get_data(sql)
            data=int(data[0]['requests_math'])+1
            requests_math_data=submmit.objects.get(article_id=article_id)
            requests_math_data.requests_math=str(data)
            requests_math_data.save()
            if goods:
                pass
            else:
                good.objects.create(author_id=openid, article_id=article_id)
            sql = "SELECT article_id,is_good,is_keep FROM share_good where author_id='%s'and article_id='%s'" % (
            openid, article_id)
            data = get_data(sql)
            return JsonResponse(data=data,safe=False)
        else:
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
class Waitselect(APIView):
    def post(self,request):
        if request.method =='POST':
            openid = request.POST.get('openid', '')
            is_starff=userinfo.objects.get(openid=openid).is_starff
            if is_starff=='1':
                sql = "SELECT article_id,title,content,author_name,photo,touxiang FROM share_submmit where waitselect='0' order by time "
                data=get_data(sql)
                return JsonResponse(data=data,safe=False)
            else:
                return HttpResponse(status.HTTP_403_FORBIDDEN)
        else:
            return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
class Select(APIView):
    def post(self,request):
        if request.method=='POST':
            id=request.POST.get('article_id','')
            index=request.POST.get('index','')
            starff = submmit.objects.get(article_id=id)
            if index=='1':
                starff.is_pass=index
            else:
                pass
            starff.waitselect='1'
            starff.save()
            return HttpResponse(status.HTTP_201_CREATED)
class Good(APIView):
    def post(self,request):
        if request.method=='POST':
            id=request.POST.get('openid','')#用户记录的唯一标识
            article_id=request.POST.get('article_id','')#分享内容的唯一标识
            goods=good.objects.filter(author_id=id,article_id=article_id)
            if goods:
                is_good = goods[0].is_good
                goodeds = submmit.objects.get(article_id=article_id)
                if is_good=='1':
                    goodeds.gooded-=1
                    goods[0].is_good='0'
                    is_data=goods[0].is_good
                    goods[0].save()
                    goodeds.save()
                else:
                    goodeds.gooded += 1
                    goods[0].is_good = '1'
                    is_data=goods[0].is_good
                    goods[0].save()
                    goodeds.save()
                data={
                    'is_good':is_data,
                    'goodeds':goodeds.gooded
                }
                return JsonResponse(data=data,safe=False)
            else:
                return HttpResponse(status.HTTP_202_ACCEPTED)
class Postkeep(APIView):
    def post(self,request):
        if request.method=='POST':
            id = request.POST.get('openid', '')  # 用户表记录的唯一标识
            article_id = request.POST.get('article_id', '')  # 分享内容的唯一标识
            goods = good.objects.filter(author_id=id, article_id=article_id)
            if goods:
                is_keep = goods[0].is_keep
                if is_keep=='1':
                    goods[0].is_keep = '0'
                    is_data=goods[0].is_keep
                    goods[0].save()
                else:
                    goods[0].is_keep = '1'
                    is_data = goods[0].is_keep
                    goods[0].save()
                data={
                    'is_keep':is_data
                }
                return JsonResponse(data=data,safe=False)
            else:
                return HttpResponse(status.HTTP_202_ACCEPTED)
class Getkeep(APIView):
    def post(self,request):
        if request.method=='POST':
            openid=request.POST.get('openid','')
            goods = good.objects.filter(author_id=openid, is_keep='1')
            data_all=[]
            if goods:
                for i in range(len(goods)):
                    article_id=goods[i].article_id
                    sql = "SELECT title,content,article_id,author_name,touxiang,gooded,requests_math FROM share_submmit where article_id='%s'and is_pass='1' order by time "%(article_id)
                    data=get_data(sql)
                    print(data[0])
                    data_all.append(data[0])
                return JsonResponse(data=data_all, safe=False)
            else:
                data={}
                return JsonResponse(data=data,safe=False)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes
@csrf_exempt
@parser_classes(('MultiPartParser',))
class upload_handle(APIView):
    def post(self,request):
        if "file" in request.FILES:
        # 1、获取上传文件的处理对象
            f = request.FILES["file"]
            picture = PicTest()
            picture.goods_pic = f
            picture.save()
            return HttpResponse('上传成功')
