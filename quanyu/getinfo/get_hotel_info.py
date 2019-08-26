# from selenium import webdriver
# from selenium.webdriver import ActionChains  #这个是模仿鼠标动作的
# from selenium.webdriver.common.by import By #这个是设置查找方式的By.ID,By.CSS_SELECTOR
# from selenium.webdriver.common.keys import Keys #这个是模拟键盘按键操作的
# from selenium.webdriver.support import expected_conditions  #这个是标注状态的
# from selenium.webdriver.support.wait import WebDriverWait #这个是等待页面加载某些元素
# from selenium.webdriver.chrome.options import Options#设置谷歌无头浏览器
# import time
# import pymysql
# from lxml import etree
# import requests
# import re
# def collect(name,location,pinfen,customers,price,images,dizhi):
#     database = pymysql.connect(host='localhost', user='root', password='Ab103827', port=3306, db='quanyu')
#     corsor=database.cursor()
#     sql="INSERT IGNORE INTO hotel(hotel_name,location,pinfen,customer,price,images,city) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(name,location,
#                                                     pinfen,customers,price,images,dizhi)
#     print(name,location, pinfen,customers,price,images,dizhi)
#     try:
#         corsor.execute(sql)
#         database.commit()
#     except:
#         database.rollback()
#     database.close()
# def hotel_info(dizhi):
#     chrome_options = Options()
#     # 无头浏览器
#     chrome_options.add_argument('--headless')
#     browser = webdriver.Chrome(chrome_options=chrome_options)
#     url="https://hotel.meituan.com/%s/"%(dizhi)
#     browser.get(url)
#     browser.maximize_window()
#     time.sleep(2)
#     browser.find_element_by_class_name("search-btn").click()
#     time.sleep(1)
#     contents = etree.HTML(browser.page_source)
#     name = []
#     types = []
#     location = []
#     pinfen = []
#     pinfen1s = []
#     pinfen3s = []
#     customers = []
#     price = []
#     data = {}
#     images = []
#     title1 = contents.xpath('//div[@class="info-wrapper"]/h3/a//text()')  # 获取酒店名以及类型
#     for i in range(len(title1)):
#         if i % 2 == 1:
#             name2 = title1[i].split()[0]
#             name.append(name2)
#     leixing = contents.xpath('//div[@class="info-wrapper"]/h3/span//text()')
#     for i in range(len(leixing)):
#         types.append(leixing[i])
#     content = contents.xpath('//div[@class="poi-address"]//text()')
#     for i in range(len(content)):  # 获取酒店详细地址
#         if i % 3 == 1:
#             location2 = content[i].split()[0]
#             location.append(location2)
#     pinfen4 = contents.xpath('//div[@class="poi-grade"]//text()')  # 获取酒店评价
#     for i in range(len(pinfen4)):
#         if i % 3 == 0:
#             pinfen1 = pinfen4[i].split()[0]
#             pinfen1s.append(pinfen1)
#         if i % 3 == 2:
#             pinfen3s.append(pinfen4[i])
#     for i in range(20):
#         s1 = ' '
#         seq = (pinfen1s[i], '分', pinfen3s[i])
#         pinfenss = s1.join(seq)
#         pinfen.append(pinfenss)
#     customer = contents.xpath('//div[@class="poi-buy-num"]//text()')
#     for i in range(len(customer)):
#         customers.append(customer[i])
#     prices = contents.xpath('//div[@class="poi-price"]/em//text()')
#     for i in range(len(prices)):
#         price.append(prices[i])
#     img = contents.xpath('//div[@class="picture-wrapper"]/a/img/@src')
#     for i in range(len(img)):
#         images.append(img[i])
#     for i in range(20):
#         data.setdefault(i, {})['hotel_name'] = name[i]
#         data.setdefault(i, {})['hotel_location'] = location[i]
#         data.setdefault(i, {})['hotel_pinfen'] = pinfen[i]
#         data.setdefault(i, {})['hotel_customer'] = customers[i]
#         data.setdefault(i, {})['hotel_price'] = price[i]
#         data.setdefault(i, {})['hotel_img'] = images[i]
#         collect(name[i],location[i],pinfen[i],customer[i],price[i],images[i],dizhi)
# if __name__ == '__main__':
#     dizhi=['loudi','beijing','tianjing','shanghai','changsha','guangzhou','chengdu','chongqing','nanjing','wuhan','xian','hangzhou']
#     for i in range(len(dizhi)):
#         hotel_info(dizhi[i])
#         print(dizhi[i],'爬取成功')
#         time.sleep(5)
#
