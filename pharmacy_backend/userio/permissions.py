from rest_framework.permissions import BasePermission
from .models import OrganizationUser


# class CustomUserPermissionWe(BasePermission):
#     def has_permission(self,request,view):
#         if request.user.is_authenticated:
#             if (request.user.is_staff or request.user.is_superuser) and request.user.role !='CUSTOMER':
#                 return True
#         return False

class CustomUserPermission(BasePermission):
    def has_permission(self,request,view):
        user=request.user
        super=user.is_superuser
        if user.is_authenticated:
            if user.is_superuser:
                return True
            try:
                org_user= OrganizationUser.objects.get(user=user)
                if org_user.is_staff and org_user.role != 'CUSTOMER':
                    return True
            except OrganizationUser.DoesNotExist:
                pass
            return False
