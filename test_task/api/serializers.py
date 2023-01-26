from api.models import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'brand',
            'name',
            'license_plate',
            'body_type',
            'color',
            'owner',)
