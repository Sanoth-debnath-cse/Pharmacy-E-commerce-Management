from rest_framework import generics
from productio.rest.serializer.serializer import ProductCategorySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from userio.permissions import CustomUserPermission

from userio.models import OrganizationUser

class ProductCategoryCreateAPIView(generics.CreateAPIView):
    serializer_class=ProductCategorySerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[CustomUserPermission]
    def perform_create(self, serializer):
        user=self.request.user

        try:
            org_user=OrganizationUser.objects.get(user=user)
            serializer.save(organization=org_user.organization)
        except OrganizationUser.DoesNotExist:
            return Response("User Have no Organizations")

