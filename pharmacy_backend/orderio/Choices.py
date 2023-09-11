from django.db import models

class DeliveryStatusChoice(models.TextChoices):
    PROCESSING='PROCESSING','processing'
    SHIPPED='SHIPPED','shipped'
    DELIVERED='DELIVERED','delivered'
    RECEIVED='RECEIVED','received'
    