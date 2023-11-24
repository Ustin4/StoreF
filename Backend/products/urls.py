from django.urls import path

from .views import (
    DeviceListCreateView,
    DeviceRetrieveUpdateDestroyView,
    DeviceBrandListCreateView,
    DeviceBrandRetrieveUpdateDestroyView,
    DeviceTypeListCreateView,
    DeviceTypeRetrieveUpdateDestroyView,
)


urlpatterns = [
    path('device/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('device/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
    path('brand/', DeviceBrandListCreateView.as_view(), name='brand-list-create'),
    path('brand/<int:pk>/', DeviceBrandRetrieveUpdateDestroyView.as_view(), name='brand-retrieve-update-destroy'),
    path('type/', DeviceTypeListCreateView.as_view(), name='type-list-create'),
    path('type/<int:pk>/', DeviceTypeRetrieveUpdateDestroyView.as_view(), name='type-retrieve-update-destroy'),
 ]