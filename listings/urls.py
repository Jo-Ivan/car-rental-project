from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('listing_create', views.listing_create, name='listing_create'),
    path('delete/<int:listing_id>',
         views.listing_delete, name='listing_delete'),
    path('edit/<int:listing_id>',
         views.listing_edit, name='listing_edit')
]
