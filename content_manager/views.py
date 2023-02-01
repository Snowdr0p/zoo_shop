"""content views"""
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from shop_items.models import Animal


def get_index(request: WSGIRequest) -> HttpResponse:
    """Главная страница"""
    animals = Animal.objects.filter(show=True)

    context = {
        "categories": animals,
    }

    return render(
        request=request,
        template_name='content_manager/index.html',
        context=context,
    )
