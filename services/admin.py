from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image', 'created_at', 'updated_at', 'category')

class CagtegoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



admin.site.register(Category, CagtegoryAdmin)
admin.site.register(Product, ProductAdmin)