
import requests
# Create your tests here.
data={
    'code':'043cO74a1872zN1NML1a1kls4a1cO74z',
    'username':'tao',
    'images':'iama/as',
    'location':'长沙',
    'openid':'1'
}
r=requests.post(url='http://192.168.1.100:8090/user/login/',data=data)
print(r.text)