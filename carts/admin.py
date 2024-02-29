from django.contrib import admin

from .models import Cart

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ['user', 'product', 'qty']
    search_fields = ['user']
