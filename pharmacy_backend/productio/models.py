from django.db import models
import uuid
from userio.models import Organization

from django.utils.text import slugify

class ProductCategory(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,related_name='product_categories')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=255,null=True)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='products')
    product_unit_price=models.DecimalField(max_digits=50,decimal_places=2)
    product_quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return self.name

    

class Tag(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    name=models.CharField(max_length=255)
    product=models.ManyToManyField(Product)

    def __str__(self):
        return self.name



