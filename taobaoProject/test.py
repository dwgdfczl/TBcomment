"""
import requests
import re
import json
import jsonpath

url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=44359701868&spuId=326435340&sellerId=368609005&order=3&currentPage=5'

data = requests.get(url).text

data1 = data.replace('jsonp128(','').replace(')','')
# print(type(eval(data1)))

str_data = json.loads(data1)
# print(type(str_data))

comment = jsonpath.jsonpath(str_data,'$..rateContent')
for i in comment:
	print(i.strip())
#将jsonurl返回的结果转化为正常json格式的代码，也不用管

"""
"""
import re

str_href = '//detail.tmall.com/item.htm?id=537118267969&skuId=3207895064628&standard=1&user_id=2956756848&cat_id=2&is_b=1&rn=8a745af933d023788893466aa898fc2b'

id_href = re.findall(r"\?id=(.*?)&",str_href)
print(id_href)

#正则练习，不用管，其实是正则不记得了，在这做test

"""