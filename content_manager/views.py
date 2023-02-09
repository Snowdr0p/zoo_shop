"""content views"""
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from shop_items.models import Animal
from news.models import News
from reviews.forms import ReviewForm
from reviews.models import Review


def get_index(request: WSGIRequest) -> HttpResponse:
    """Главная страница"""
    animals = Animal.objects.filter(show=True)
    news = News.objects.filter(show=True).order_by('-pub_date')
    reviews = Review.objects.filter(show=True).order_by('-pub_date')[:10]

    context = {
        "categories": animals,
        "news": news,
        "reviews": reviews,
        "review_form": ReviewForm()
    }

    return render(
        request=request,
        template_name='content_manager/index.html',
        context=context,
    )
