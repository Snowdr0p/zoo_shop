"""content views"""
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def get_index(request: WSGIRequest) -> HttpResponse:
    """Главная страница"""
    context = {

    }

    return render(
        request=request,
        template_name='content_manager/index.html',
        context=context,
    )
