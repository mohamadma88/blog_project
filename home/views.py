from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Article


def home(request):
    article = Article.objects.order_by('created_at')[:3]
    return render(request, 'home/index.html', context={'article': article})
