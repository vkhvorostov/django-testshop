from django import forms
from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html

# Register your models here.
from .models import Shop, Category, Product

class ShopAdminForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        widgets = {
            'imageUrl': forms.ClearableFileInput(),
        }

class ShopAdmin(admin.ModelAdmin):
    form = ShopAdminForm
    list_display = ('title', 'display_image')
    search_fields = ['title']

    def display_image(self, obj):
        return format_html('<img src="{}" height="75" />', settings.MEDIA_URL + str(obj.imageUrl))
    display_image.short_description = 'Image'

admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)
admin.site.register(Product)