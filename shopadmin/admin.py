from django import forms
from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html

# Register your models here.
from .models import Shop, Category, Product, ProductImage

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

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'child_count')
    list_display_links = ('title',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        parent = request.GET.get('parent')
        if parent:
            queryset = queryset.filter(parent_id=parent)
        else:
            queryset = queryset.filter(parent_id=None)
        return queryset

    def child_count(self, obj):
        childs_number = Category.objects.filter(parent_id=obj.id).count()
        return format_html('<a href="?parent={}">{}</a>', obj.id, childs_number)
    child_count.short_description = 'Child Categories'

class ProductImagesAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ('title', 'first_image')
    list_display_links = ('title',)

    class Meta:
        model = Product

    def first_image(self, obj):    
        return format_html('<img src="{}" height="75" />', obj.images.order_by("id")[0].image.url)

#admin.site.register(ProductImage)    
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)