from accounts.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = ("id", "user", "email", "first_name", "address", "location")

        extra_kwargs = {"location": {"read_only": True}}
