from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserProfile, Landmark, Tour, Booking, Guide, GuideBookingStatus
from .serializers import UserProfileSerializer, LandmarkSerializer, TourSerializer, BookingSerializer, GuideSerializer, GuideBookingStatusSerializer
from rest_framework.filters import SearchFilter
from .filters import LandmarkFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LandmarkViewSet(viewsets.ModelViewSet):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = LandmarkFilter
    search_fields = ['name_landmark']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GuideBookingStatusViewSet(viewsets.ModelViewSet):
    queryset = GuideBookingStatus.objects.all()
    serializer_class = GuideBookingStatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
