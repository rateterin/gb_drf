from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'last_name', 'first_name')
    list_display_links = ('pk', 'username', 'email')
    list_editable = ('first_name', 'last_name')

