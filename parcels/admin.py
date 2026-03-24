from django.contrib import admin
from .models import Parcel, TrackingEvent


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('id', 'tracking_number', 'recipient_name', 'status', 'created_at')
    search_fields = ('tracking_number', 'recipient_name', 'sender_name')
    list_filter = ('status', 'created_at')


@admin.register(TrackingEvent)
class TrackingEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'parcel', 'status', 'created_at')
    search_fields = ('parcel__tracking_number',)
    list_filter = ('status', 'created_at')
