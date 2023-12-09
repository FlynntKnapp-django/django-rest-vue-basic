from rest_framework import serializers

from favorites.models import Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = (
            "name",
            "description",
        )
