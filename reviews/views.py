from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .forms import ReviewForm
from .models import Review


def create_review(request: HttpRequest) -> HttpResponse:
    """Creates a review"""
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = Review(**review_form.cleaned_data)

            review.save()

    return redirect(reverse('index'), request)
