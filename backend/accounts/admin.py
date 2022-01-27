from django.contrib import admin
from .models import AccountModel


@admin.register(AccountModel)
class Account(admin.ModelAdmin):
    list_display = ('user', 'subject', 'state',
                    'price', 'created', 'updated')
    list_editable = ('state',)
    list_filter = ('created',)
