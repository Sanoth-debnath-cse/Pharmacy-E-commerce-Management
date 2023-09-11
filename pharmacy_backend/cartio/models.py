from django.db import models
from userio.models import User
from productio.models import Product
import uuid

class Cart(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product,related_name='carts',through='CartItem')
    is_order=models.BooleanField(default=False)

    def __str__(self):
        return f"Cart for {self.user.first_name}"
    
class CartItem(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.product_quantity} x {self.product.name} in {self.cart}"

