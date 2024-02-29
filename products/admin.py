from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'avatar', 'qty']
    list_filter = ['category']
    search_fields = ['title']
