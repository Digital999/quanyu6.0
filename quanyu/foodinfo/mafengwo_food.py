# import requests
# import pymysql
# from lxml import etree
# import time
# def firststep(url):
#
#     r=requests.get(url=url,headers=set_header)
#     contents=etree.HTML(r.text)
#     neirong=contents.xpath('//ul[@class="poi-list"]//li/div[@class="title"]/h3/a/@href')
#     for i in range(len(neirong)):
#         url='http://www.mafengwo.cn'+neirong[i]
#         secondstep(url)
#         time.sleep(2)
# def secondstep(url):
#     r=requests.get(url,headers=set_header)
#     contents=etree.HTML(r.text)
#     name=contents.xpath('//h1/text()')
#     images=contents.xpath('//div[@class="pic-r"]/a/img/@src')
#     pinfen=contents.xpath('//span[@class="score-info"]/em/text()')
#     jianyi=contents.xpath('//span[@class="comm-info"]/em/text()')
#     location=contents.xpath('//i[@class="icon-location"]/../text()')
#     locations=str(location).split('地址：')[1].split('\'')[0]
#     star='★★★★'
#     collect(name,images,pinfen,jianyi,locations,star)
# def collect(name,images,pinfen,jianyi,location,star):
#     database = pymysql.connect(host='localhost', user='root', password='Ab103827', port=3306, db='quanyu',charset='utf8')
#     corsor = database.cursor()
#     sql = "INSERT IGNORE INTO mafengwo_food(food_name,images,pinfen,jianyi,location,star) VALUES (%s,%s,%s,%s,%s,%s);"
#     print(name,images,pinfen,jianyi,location,star)
#     try:
#         corsor.execute(sql,[name,images,pinfen,jianyi,location,star])
#         database.commit()
#     except:
#         print('失败')
#         database.rollback()
#     database.close()
#     corsor.close()
# if __name__ == '__main__':
#     set_header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 '
#                       'Safari/537.36',
#         'Host': 'www.mafengwo.cn',
#     }
#     url = 'http://www.mafengwo.cn/cy/63584/gonglve.html'
#     firststep(url)