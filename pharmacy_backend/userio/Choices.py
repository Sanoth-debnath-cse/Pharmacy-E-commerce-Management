from django.db import models

class RoleChoices(models.TextChoices):
    OWNER='OWNER','owner'
    ADMIN='ADMIN','admin'
    MANAGER='MANAGER','manager'
    STAFF='STAFF','staff'
    CUSTOMER='CUSTOMER','customer'