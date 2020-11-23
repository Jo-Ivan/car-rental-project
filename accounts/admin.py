from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at', 'first_name', 'last_name')
    list_display_links = ('id', 'email')
    list_per_page = 30


admin.site.register(Account, AccountAdmin)
