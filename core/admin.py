from django.contrib import admin
from core.models import Product, Tag


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'price',
    )
    search_fields = (
        'title', 'description', 'tags'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
