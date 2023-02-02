"""content views"""
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from shop_items.models import Animal
from news.models import News


def get_index(request: WSGIRequest) -> HttpResponse:
    """Главная страница"""
    animals = Animal.objects.filter(show=True)
    news = News.objects.filter(show=True).order_by('-pub_date')

    context = {
        "categories": animals,
        "news": news,
    }

    return render(
        request=request,
        template_name='content_manager/index.html',
        context=context,
    )
