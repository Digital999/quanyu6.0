from rest_framework.views import APIView
from .models import userinfo
import requests
from rest_framework import status
import json
from django.http import JsonResponse
class user_login(APIView):
    def post(self,request):
        # serilizer=userinfoSerializer(data=request.data)
        #判断提交的格式是否正确
        if request.method=='POST':
            code=request.data['code']
            username=request.data['username']
            images=request.data['images']
            location=request.data['location']
            keys=json.loads(loginView(code))
            session_key=keys['session_key']
            openid=keys['openid']
            #判断是否为新用户
            if userinfo.objects.filter(openid=openid):
                is_starffs = userinfo.objects.get(openid=openid).is_starff
                #如果不为新用户,则更新当前用户的信息
                userinfo.objects.update(username=username, images=images, location=location)
            else:
                #如果是新用户,则将用户信息新增到数据库中
                userinfo.objects.create(username=username, images=images, location=location, openid=openid)
                is_starffs='0'

            author_id = userinfo.objects.get(openid=openid).id
            data = {
                'author_id':author_id,
                'session_key': session_key,
                'openid': openid,
                'index': is_starffs
            }
            return JsonResponse(data=data)

#向微信服务器发起get请求,获取session_key以及openid
def loginView(code):
    appid = 'wx7b918651b55b93c6'
    appsecret = 'ab81c6412ebd11fb2eb0dd441880c902'
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
    appid, appsecret, code)
    r=requests.get(url=url)
    return r.text