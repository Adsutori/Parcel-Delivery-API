from rest_framework import serializers
from .models import Parcel, TrackingEvent


class TrackingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingEvent
        fields = ['id', 'status', 'description', 'created_at']


class ParcelSerializer(serializers.ModelSerializer):
    tracking_events = TrackingEventSerializer(many=True, read_only=True)

    class Meta:
        model = Parcel
        fields = [
            'id',
            'tracking_number',
            'sender_name',
            'recipient_name',
            'delivery_address',
            'city',
            'postal_code',
            'country',
            'status',
            'description',
            'created_at',
            'updated_at',
            'tracking_events',
        ]
        read_only_fields = ['id', 'tracking_number', 'created_at', 'updated_at', 'tracking_events']
