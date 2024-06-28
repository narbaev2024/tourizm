from rest_framework import serializers
from .models import UserProfile, Landmark, Tour, Booking, Guide, GuideBookingStatus

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmark
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'

class GuideBookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideBookingStatus
        fields = '__all__'
