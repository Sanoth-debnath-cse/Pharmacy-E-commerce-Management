from rest_framework import generics
from userio.rest.serializer.serializer import UserSerializer, UserViewSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from userio.permissions import CustomUserPermission
from userio.models import User


class RegistrationUserView(generics.CreateAPIView):
    serializer_class=UserSerializer
    permission_classes=(AllowAny,)


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class=UserSerializer
    authentication_classes=[JWTAuthentication]

    def get_object(self):
        return self.request.user
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class=UserViewSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[CustomUserPermission]

class UserDataRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserViewSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[CustomUserPermission]
    lookup_field='uid'

