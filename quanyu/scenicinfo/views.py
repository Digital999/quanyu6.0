from rest_framework.views import APIView
from django.http import JsonResponse
from datastyle_change import get_data
from change_to_pinyin import word
class scenic_info(APIView):
    def post(self, request):
        if request.method == 'POST':
            dizhi = request.data['dizhi']
            pinyin = word(dizhi)
            sql = "SELECT * FROM mafengwo_scenic where city='%s'" % (pinyin)
            data=get_data(sql)
            return JsonResponse(data=data, safe=False)



