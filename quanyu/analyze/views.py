from rest_framework.views import APIView
from rest_framework.response import Response
from .models import customer_age,customer_from,customer_method,customer_staytime,customer_team,customer_tools
from .serilizer import Mycustomerage_Serializer,Mycustomerteam_Serializer,Mycustomerstaytime_Serializer,\
    Mycustomerfrom_Serializer,Mycustomermethod_Serializer,Mycustomertools_Serializer
class age_analyze(APIView):
    def post(self,request):
        if request.method == 'POST':
            s = request.POST.get('dizhi','')
            queryset = customer_age.objects.filter(location=s)
            serializer = Mycustomerage_Serializer(queryset, many=True)
            return Response(serializer.data)
class team_analyze(APIView):
    def post(self,request):
        if request.method == 'POST':
            s = request.data['dizhi']
            queryset = customer_team.objects.filter(location=s)
            serializer = Mycustomerteam_Serializer(queryset, many=True)
            return Response(serializer.data)
class staytime_analyze(APIView):
    def post(self,request):
        if request.method == 'POST':
            s = request.data['dizhi']
            queryset = customer_staytime.objects.filter(location=s)
            serializer = Mycustomerstaytime_Serializer(queryset, many=True)
            return Response(serializer.data)
class from_analyze(APIView):
    def post(self,request):
        if request.method == 'POST':
            s = request.data['dizhi']
            queryset = customer_from.objects.filter(location=s)
            serializer = Mycustomerfrom_Serializer(queryset, many=True)
            return Response(serializer.data)
class tools_analyze(APIView):
    def post(self,request):
        if request.method == 'POST':
            s = request.data['dizhi']
            queryset = customer_tools.objects.filter(location=s)
            serializer = Mycustomertools_Serializer(queryset, many=True)
            return Response(serializer.data)
class method_analyze(APIView):
    def post(self,request):
        if request.method == 'POST':
            s = request.data['dizhi']
            queryset = customer_method.objects.filter(location=s)
            serializer = Mycustomermethod_Serializer(queryset, many=True)
            return Response(serializer.data)

# def word(dizhi):
#     s = ''
#     for i in pypinyin.pinyin(dizhi, style=pypinyin.NORMAL):
#         s += ''.join(i)
#     return s

