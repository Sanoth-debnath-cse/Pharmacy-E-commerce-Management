from django.db import models
from userio.models import User,Organization
from productio.models import Product
import uuid

class Rating(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='rating')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    rated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=('user','product')

    def __str__(self):
        return f"Rating of {self.rating} stars by {self.user.first_name} for {self.product.name}"


