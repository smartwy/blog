from django.shortcuts import render

# Create your views here.
import requests

def req(request):
	data = requests.get('http://www.jxntv.cn/data/jmd-jxtv2.html?callback=list&_=1454376870403')
	data.encoding = 'utf-8'
	return render(request, 'req.html', {'data':data.text})