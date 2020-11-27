from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'is_rented', 'borough', 'price', 'user')
    list_display_links = ('id', 'title')
    list_filter = ('user',)
    list_editable = ('is_published', 'is_rented')
    search_fields = ('title', 'description', 'borough', 'price')
    list_per_page = 30


admin.site.register(Listing, ListingAdmin)
