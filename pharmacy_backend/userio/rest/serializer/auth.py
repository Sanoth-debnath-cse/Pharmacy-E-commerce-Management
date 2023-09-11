from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model


from rest_framework.exceptions import AuthenticationFailed

from rest_framework import serializers


from userio.helper.tokens import TokenHelper


User = get_user_model()


class PublicUserTokenSerializer(serializers.Serializer):
    phone = serializers.SlugRelatedField(
        queryset=User.objects.filter(), slug_field="phone", write_only=True
    )

    password = serializers.CharField(write_only=True)

    refresh = serializers.CharField(max_length=255, read_only=True)

    access = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        user = attrs.get("phone")

        password = attrs.get("password")

        if not user.check_password(password):
            raise AuthenticationFailed()

        return attrs

    def create(self, validated_data):
        user = validated_data.get("phone")

        refresh_token, access_token = TokenHelper().create_token(user)

        validated_data["refresh_token"] = refresh_token

        validated_data["access_token"] = access_token

        return validated_data
