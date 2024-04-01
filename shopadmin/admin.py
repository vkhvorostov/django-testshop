from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Shop, Category, Product

class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image')
    search_fields = ['title']

    def display_image(self, obj):
        return format_html('<img src="{}" height="75" />', obj.imageUrl)
    display_image.short_description = 'Image'

admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)
admin.site.register(Product)