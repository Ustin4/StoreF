from django.db import models


class DeviceType(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class DeviceBrand(models.Model):
    name = models.CharField(max_length=128)
    types = models.ManyToManyField(DeviceType, null=True, blank=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products_images', null=True, blank=True)
    types = models.ForeignKey(to=DeviceType, on_delete=models.CASCADE)
    brand = models.ForeignKey(to=DeviceBrand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        return f"Продукт: {self.name} | Тип: {self.types.name} | Бренд: {self.brand.name}"





