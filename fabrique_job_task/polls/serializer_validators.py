from rest_framework import serializers

from users.models import UserProfile


def user_existence_validator(user_identifier):
    try:
        UserProfile.objects.get(identifier=user_identifier)
    except UserProfile.DoesNotExist:
        raise serializers.ValidationError(
            f'No user with identifier: {user_identifier}'
        )
    return user_identifier
