from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()
    title = 'Новости'
    context = {
        'title': title,
        'news': news,
    }
    return render(request, 'news/index.html', context)
