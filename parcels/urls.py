from django.urls import path
from .views import HealthCheckView, ParcelListCreateView, ParcelDetailView, TrackingEventListView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('parcels/', ParcelListCreateView.as_view(), name='parcel-list-create'),
    path('parcels/<int:pk>/', ParcelDetailView.as_view(), name='parcel-detail'),
    path('parcels/<int:parcel_id>/tracking-events/', TrackingEventListView.as_view(), name='tracking-event-list'),
]
