from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'purchase_price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_title', 'version_number', 'current_version',)
    list_filter = ('product',)
