# -*- coding: utf-8 -*-
#该爬虫文件是直接访问json接口爬取评论数据

import scrapy
from taobaoProject.items import TaobaoprojectItem
import requests
import json
import jsonpath

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['www.tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%C3%E6%C4%A4']

    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=44359701868&spuId=326435340&sellerId=368609005&order=3&currentPage={}'  #json接口的url,去掉了一些没用的参数
    page = 1

    def start_requests(self):
    	url = self.url.format(self.page)  #拼接url
    	yield scrapy.Request(url,callback=self.parse,dont_filter=True)

    def parse(self, response):
    	# data = requests.get(url).text
    	data1 = response.text.replace('jsonp128(','').replace(')','')  #获取jsonurl返回的内容并转化为json格式
    	str_data = json.loads(data1)
    	comment = jsonpath.jsonpath(str_data,'$..rateContent')  #通过jsonpath提取，详情请百度
    	for i in comment:
    		item = TaobaoprojectItem()
    		item['评论'] = i
    		yield item



"""
# url1 = 'https://rate.tmall.com/list_detail_rate.htm?itemId=41681863329&spuId=326435340&sellerId=368609005&order=3&currentPage=50'  
# url11 = 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.8.3efd6997fwWepp&id=41681863329&skuId=3664381075113&areaId=110100&standard=1&user_id=1077716829&cat_id=2&is_b=1&rn=e055dbf47ac3c22d3a0a33c3c13f8727'

# url2 = 'https://rate.tmall.com/list_detail_rate.htm?itemId=4359111383&spuId=274700274&sellerId=368609005&order=3&currentPage=1'
# url22 = 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.39.3efd6997fwWepp&id=4359111383&skuId=3499415010755&areaId=110100&standard=1&user_id=368609005&cat_id=2&is_b=1&rn=e055dbf47ac3c22d3a0a33c3c13f8727'
"""