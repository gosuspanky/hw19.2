from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_per_purchase', 'category', 'img', 'is_published')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'content', 'img', 'created_at', 'is_published', 'views_count')
    list_filter = ('name', )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'version_num', 'version_name', 'is_active_version',)
