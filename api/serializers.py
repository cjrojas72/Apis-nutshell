from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color']


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['size', 'brand_name', 'manufacturer',
                  'colors', 'shoe_type', 'fasten_type']


# ps. Joe once helped saved two tigers he named Simba and Luna
# growing up on the African Savanna. They are now part of a Tiger Sancutary
# and he visits them every few years.
