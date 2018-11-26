#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:
from bs4 import BeautifulSoup

content = """
		<p class='c1' id='i1'>
			asdfaa<span style="font-family:NSimSun;">sdf<a>a</a>sdf</span>sdf
		</p>
		<p>
			<strong class='c2' id='i2'>asdf</strong>
			<script>alert(123)</script>
		</p>
		<h2>
			asdf
		</h2>
		"""
tags = {  # 白名单
	'p': ['class'],  # 只允许p标签的class属性
	'strong': ['id']
}
soup = BeautifulSoup(content, 'html.parser')
for tag in soup.find_all():  # 遍历所有内容
	if tag.name in tags:  # 判断是否在白名单中
		pass
	else:  # 不在白名单隐藏标签删除数据，跳到下一循环
		tag.hidden = True
		tag.clear()
		continue
	input_attrs = tag.attrs  # 获取当前标签的属性
	valid_attrs = tags[tag.name] # 白名单属性
	for k in list(input_attrs.keys()): # 遍历属性
		if k in valid_attrs: # 判断当前属性是否是白名单属性
			pass
		else:
			del tag.attrs[k] # 不是白名单属性，删除
content = soup.decode('utf-8')
print(content)



