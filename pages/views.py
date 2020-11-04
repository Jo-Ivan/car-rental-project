from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import borough_choices

from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'borough_choices': borough_choices
    }

    return render(request, 'pages/index.html', context)


def login(request):
    return render(request, 'pages/login.html')


def signup(request):
    return render(request, 'pages/signup.html')


def list(request):
    return render(request, 'pages/list.html')
