from django.contrib import admin
from .models import Product,ProductCategory,Tag

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Tag)