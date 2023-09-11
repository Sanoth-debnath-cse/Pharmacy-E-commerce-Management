from rest_framework import status

from rest_framework.response import Response

from rest_framework.generics import CreateAPIView


from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


from userio.rest.serializer.auth import PublicUserTokenSerializer


class PublicUserTokenView(CreateAPIView):
    serializer_class = PublicUserTokenSerializer
