from rest_framework.views import APIView
import pymysql
from change_to_pinyin import word
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_page


class hotel_analyze(APIView):
    def post(self,request):
        if request.method == 'POST':
            dizhi=request.POST.get('dizhi','')
            location=word(dizhi)
            db = pymysql.connect(host='47.94.243.187', user='root', password='Ab103827', port=3306, db='quanyu')
            corsor = db.cursor()
            sql = "SELECT HOTEL_NAME FROM hotel where city='%s'order by price LIMIT 5" % (location)
            try:
                corsor.execute(sql)
                data = corsor.fetchall()
            except:
                db.rollback()
            db.close()
            sql1 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[0]).split('\'')[1])
            sql2 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[1]).split('\'')[1])
            sql3 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[2]).split('\'')[1])
            sql4 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[3]).split('\'')[1])
            sql5 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[4]).split('\'')[1])
            db = pymysql.connect(host='47.94.243.187', user='root', password='Ab103827', port=3306, db='quanyu')
            corsor = db.cursor()
            try:
                corsor.execute(sql1)
                data1 = corsor.fetchall()
                corsor.execute(sql2)
                data2 = corsor.fetchall()
                corsor.execute(sql3)
                data3 = corsor.fetchall()
                corsor.execute(sql4)
                data4 = corsor.fetchall()
                corsor.execute(sql5)
                data5 = corsor.fetchall()
                data={
                    '1':data1,
                    '2':data2,
                    '3':data3,
                    '4':data4,
                    '5':data5
                }
            except:
                db.rollback()
            db.close()
            db = pymysql.connect(host='47.94.243.187', user='root', password='Ab103827', port=3306, db='quanyu')
            corsor = db.cursor()
            sql = "SELECT HOTEL_NAME FROM hotel where city='%s'order by price LIMIT 5" % (location)
            try:
                corsor.execute(sql)
                data = corsor.fetchall()
            except:
                db.rollback()
            db.close()
            sql1 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[0]).split('\'')[1])
            sql2 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[1]).split('\'')[1])
            sql3 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[2]).split('\'')[1])
            sql4 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[3]).split('\'')[1])
            sql5 = "SELECT name,nowman FROM hotelinfo_hotel where name='%s'" % (str(data[4]).split('\'')[1])
            db = pymysql.connect(host='47.94.243.187', user='root', password='Ab103827', port=3306, db='quanyu')
            corsor = db.cursor()
            try:
                corsor.execute(sql1)
                data1 = corsor.fetchall()
                corsor.execute(sql2)
                data2 = corsor.fetchall()
                corsor.execute(sql3)
                data3 = corsor.fetchall()
                corsor.execute(sql4)
                data4 = corsor.fetchall()
                corsor.execute(sql5)
                data5 = corsor.fetchall()
                data = {
                    '1': data1,
                    '2': data2,
                    '3': data3,
                    '4': data4,
                    '5': data5
                }
            except:
                db.rollback()
            db.close()
            return JsonResponse(data=data,safe=False)


