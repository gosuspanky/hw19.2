from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_per_purchase', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
