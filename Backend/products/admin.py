from django.contrib import admin

from .models import Device, DeviceBrand, DeviceType


admin.site.register(Device)
admin.site.register(DeviceBrand)
admin.site.register(DeviceType)
