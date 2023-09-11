from django.db import models
import uuid
from userio.models import User,Organization
from productio.models import Product
from .Choices import DeliveryStatusChoice


class Order(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    delivery_address=models.CharField(max_length=255,blank=True)
    Organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    is_order=models.BooleanField(default=False)

class OrderItme(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    unit_price=models.PositiveIntegerField(default=0)

class DeliveryStatus(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    is_cancel=models.BooleanField(default=False)
    status=models.CharField(max_length=20,choices=DeliveryStatusChoice.choices,null=True)







