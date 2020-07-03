from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ArticlePost


# 视图函数
def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    context = {'articles':articles}
    return  render(request, 'article/list.html', context)
