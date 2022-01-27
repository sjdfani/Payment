from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserModel(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'is_staff', 'is_superuser')
    list_editable = ('is_staff', 'is_superuser')
