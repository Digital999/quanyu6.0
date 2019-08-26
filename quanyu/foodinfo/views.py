from rest_framework.views import APIView
from django.http import JsonResponse
from datastyle_change import get_data
import pypinyin
class info_answer(APIView):
    def post(self, request):
        if request.method == 'POST':
            dizhi = request.data['dizhi']
            pinyin = word(dizhi)
            sql = "SELECT * FROM mafengwo_food where city='%s'" % (pinyin)
            data=get_data(sql)
            return JsonResponse(data=data, safe=False)
def word(dizhi):
    s = ''
    for i in pypinyin.pinyin(dizhi, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

