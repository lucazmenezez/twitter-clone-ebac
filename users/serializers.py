from rest_framework import serializers
from .models import CustomUser
from .models import Follow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "bio", "profile_image"]


class FollowSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followed_user = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "user", "followed_user", "created_at"]
