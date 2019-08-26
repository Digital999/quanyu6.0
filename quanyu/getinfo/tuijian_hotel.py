# import pymysql
# import requests
# from lxml import etree
# url='http://www.bytravel.cn/view/index2397.html'
# set_header={
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
#     'Host':'www.bytravel.cn',
# }
# r=requests.get(url=url,headers=set_header)
# coentent=r.content.decode('gb18030','ignore')
# cotents=etree.HTML(coentent)
# article=cotents.xpath('//div[@id="tctitle"]/a/@href')
# href=[]
# for i in range(len(article)):
#     href.append('http://www.bytravel.cn'+article[i])
#
#
