from rest_framework import serializers
from .models import Device, DeviceBrand, DeviceType


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceBrandSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = DeviceBrand
        fields = '__all__'


class DeviceTypeSerializer(serializers.ModelSerializer):
    brands = DeviceBrandSerializer(many=True, read_only=True)

    class Meta:
        model = DeviceType
        fields = '__all__'
