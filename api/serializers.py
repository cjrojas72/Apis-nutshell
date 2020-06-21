from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']


class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']


class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color']


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ['size', 'brand_name', 'manufacturer',
                  'colors', 'shoe_type', 'fasten_type']
