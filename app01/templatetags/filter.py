#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def filter_type(args, set):
	if set == 'articleType_id':
		if args['articleType_id'] == 0:
			ret = '<a style="border: 5px">类型：</a><a class="active" href="article-0-%s.html">全部</a>' % args['category_id']
		else:
			ret = '<a style="border: 5px">类型：</a><a href="article-0-%s.html">全部</a>' % args['category_id']
		return mark_safe(ret)
	elif set == 'category_id':
		if args['category_id'] == 0:
			ret = '<a style="border: 5px">分类：</a><a class="active" href="article-%s-0.html">全部</a>' % args['category_id']
		else:
			ret = '<a style="border: 5px">分类：</a><a href="article-%s-0.html">全部</a>' % args['category_id']
		return mark_safe(ret)

@register.simple_tag
def filter_all(args, args1, fag):
	ret = []
	if fag == 'articleType':
		for row in args1:
			if row.id == args['articleType_id']:
				ret.append('<a class ="active" href="article-%s-%s.html">%s</a>' % (row.id, args['category_id'], row.caption))
			else:
				ret.append('<a href="article-%s-%s.html">%s</a>' % (row.id, args['category_id'], row.caption))
		return mark_safe(''.join(ret))
	elif fag == 'category':
		for row in args1:
			if row.id == args['category_id']:
				ret.append('<a class ="active" href="article-%s-%s.html">%s</a>' % (args['articleType_id'], row.id, row.caption))
			else:
				ret.append('<a href="article-%s-%s.html" >%s</a>' % (args['articleType_id'], row.id, row.caption))
		return mark_safe(''.join(ret))

