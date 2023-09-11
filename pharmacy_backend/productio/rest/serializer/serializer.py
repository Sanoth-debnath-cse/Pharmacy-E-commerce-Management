from rest_framework import serializers
from productio.models import ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields=['name','organization']
        read_only_fields=['organization']
