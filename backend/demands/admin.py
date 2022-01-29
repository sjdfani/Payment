from django.contrib import admin
from .models import Demands


@admin.register(Demands)
class DemandsAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'date', 'created', 'status')
    list_editable = ('status',)
    list_filter = ('user',)
