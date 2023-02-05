from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse


def create_review(request: HttpRequest) -> HttpResponse:
    """Creates a review"""
    return redirect(reverse('index'), request)
