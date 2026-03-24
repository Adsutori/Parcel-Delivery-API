from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Parcel, TrackingEvent
from .serializers import ParcelSerializer, TrackingEventSerializer


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"message": "Parcel Delivery API is working"})


class ParcelListCreateView(generics.ListCreateAPIView):
    queryset = Parcel.objects.all().order_by('-created_at')
    serializer_class = ParcelSerializer


class ParcelDetailView(generics.RetrieveAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer


class TrackingEventListView(generics.ListAPIView):
    serializer_class = TrackingEventSerializer

    def get_queryset(self):
        parcel_id = self.kwargs['parcel_id']
        return TrackingEvent.objects.filter(parcel_id=parcel_id).order_by('-created_at')