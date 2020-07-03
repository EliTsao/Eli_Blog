from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ArticlePost
import markdown


# 视图函数
def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)

    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite'
                                     ]
                                     )
    # 需要传递给模板的对象
    context = {'article': article}
    # 载入模板，并返回context
    return render(request, 'article/detail.html', context)
