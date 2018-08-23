# -*- coding: utf-8 -*-
#该爬虫文件是先获取商品详情页的href(即url)但是不进入详情页,通过正则获取href中的id,并将其拼接到jsonurl中，即可实现对多个商品的评论进行爬取

import scrapy
from taobaoProject.items import TaobaoprojectItem
import requests
import json
import re
import jsonpath

class TmSpider(scrapy.Spider):
    name = 'tm'
    allowed_domains = ['www.tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%C3%E6%C4%A4']

    json_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId=368609005&order=3&currentPage={}'

    page = 3


    def start_request(self):
    	#发送请求
    	for url in start_urls:
    		yield scrapy.Request(url, callback=self.parse,dont_filter=True)

    def parse(self, response):
        content_div = response.xpath('//div[@id="J_ItemList"]/div[@class="product  "]')
        for content in content_div[10:]:
        	href = content.xpath('.//div[@class="productImg-wrap"]/a/@href').extract()[0]
        	# print('*'*50)
        	# print(href)
        	# print('*'*50)
        	# print(len(href))
        	id_href = re.findall(r"\?id=(.*?)&",href)

        	#获取id,并且拼接到jsonurl中。


        	if id_href:
        		comment_url = self.json_url.format(id_href[0],self.page)
        		yield scrapy.Request(comment_url,callback=self.get_comments,dont_filter=True)
        	else:
        		print('error')

    def get_comments(self, response):
    	data1 = response.text.replace('jsonp128(','').replace(')','')
    	str_data = json.loads(data1)
    	comment = jsonpath.jsonpath(str_data,'$..rateContent')
    	# print('*'*40)
    	# print(comment)
    	# print('*'*40)
    	for i in comment:
    		item = TaobaoprojectItem()
    		item['评论'] = i
    		yield item

