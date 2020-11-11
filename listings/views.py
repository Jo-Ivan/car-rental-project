from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .choices import borough_choices

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by(
        '-list_date').filter(is_published=True)

    # Car
    if 'cars' in request.GET:
        cars = request.GET['cars']
        if cars:
            queryset_list = queryset_list.filter(
                car__icontains=cars)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    # Boroughs
    if 'borough' in request.GET:
        borough = request.GET['borough']
        if borough:
            queryset_list = queryset_list.filter(
                borough__iexact=borough)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'borough_choices': borough_choices,
    }

    return render(request, 'listings/search.html', context)
