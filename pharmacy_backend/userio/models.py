from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from .Choices import RoleChoices

class UserManager(BaseUserManager):
    def create_user(self,phone_number,password=None,**extra_fields):
        if not phone_number:
            raise ValueError("User must have to input correct Phone number")
        user=self.model(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,phone_number,password):
        user=self.create_user(phone_number,password)
        user.email=''
        user.first_name='Main'
        user.last_name='Admin'
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser,PermissionsMixin):
    phone_number=PhoneNumberField(unique=True)
    email=models.EmailField(max_length=200,blank=True)
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    role=models.CharField(max_length=50,choices=RoleChoices.choices,null=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='phone_number'

    def __str__(self):
        return self.first_name+" "+self.last_name

class Organization(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
class OrganizationUser(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    role=models.CharField(max_length=50,choices=RoleChoices.choices,null=True)
    is_default=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        #return self.organization.name + self.user.first_name + self.user.last_name
        return f"{self.user.first_name} {self.user.last_name} of {self.organization.name}"

    
