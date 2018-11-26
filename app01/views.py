from django.shortcuts import render, redirect

from app01 import models

def articleH(request):
	return redirect('article-0-0.html')

def article(request, *args, **kwargs):
	articleT = models.ArticleType.objects.all()
	# articleT = models.Article.articleType_id
	categroy = models.Category.objects.all()
	# result = models.Article.objects.all()
	contation = {}
	for k,v in kwargs.items():
		kwargs[k] = int(v) # 用于判断是否选中：{% if row.id == args.category_id %}类型一致
		if v == '0':
			pass
		else:
			contation[k] = v # 构造搜索条件
	result = models.Article.objects.filter(**contation)
	return render(request, 'article.html', {'res':result,
	                                          'arty':articleT,
	                                          'cate':categroy,
	                                          'args':kwargs}) # 将上一个请求的参数反传回去，以作新的部分请求