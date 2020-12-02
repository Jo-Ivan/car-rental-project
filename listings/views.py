from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

from .choices import borough_choices

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'borough_choices': borough_choices,
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
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)


def listing_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        car = request.POST['car']
        borough = request.POST['borough']
        description = request.POST['description']
        price = request.POST['price']
        user_id = request.POST['user_id']
        photo_main = request.FILES['photo']

        listing = Listing(title=title, car=car, borough=borough,
                          description=description, price=price, user_id=user_id, photo_main=photo_main)

        listing.save()

        messages.success(request, 'Your listing has been submitted')

        return redirect('dashboard')
    return


def listing_delete(request, listing_id):
    print(listing_id)
    if request.method == 'POST':
        listing = Listing.objects.get(id=listing_id)
        listing.delete()

    return redirect('dashboard')
