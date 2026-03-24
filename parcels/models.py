from django.db import models
import uuid


class Parcel(models.Model):
    class StatusChoices(models.TextChoices):
        CREATED = 'created', 'Created'
        SENT = 'sent', 'Sent'
        IN_TRANSIT = 'in_transit', 'In transit'
        DELIVERED = 'delivered', 'Delivered'
        CANCELLED = 'cancelled', 'Cancelled'

    tracking_number = models.CharField(max_length=50, unique=True, editable=False)
    sender_name = models.CharField(max_length=255)
    recipient_name = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.CREATED
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = f"PKG-{uuid.uuid4().hex[:10].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tracking_number} - {self.recipient_name}"


class TrackingEvent(models.Model):
    parcel = models.ForeignKey(
        Parcel,
        on_delete=models.CASCADE,
        related_name='tracking_events'
    )
    status = models.CharField(max_length=20, choices=Parcel.StatusChoices.choices)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parcel.tracking_number} - {self.status}"
