from django.urls import path
from userio.rest.views.views import RegistrationUserView, ManageUserView, UserListView,UserDataRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from userio.rest.views.auth import PublicUserTokenView


urlpatterns = [
    path('registration/',RegistrationUserView.as_view(),name='registration'),
    path('tokens/',TokenObtainPairView.as_view(),name='tokens'),
    #path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('token/',PublicUserTokenView.as_view(),name="token"),
    path('me/',ManageUserView.as_view(),name='me'),
    path('we/',UserListView.as_view(),name='we'),
    path('we/<uuid:uid>',UserDataRetrieveUpdateDestroyAPIView.as_view(),name='we')

]