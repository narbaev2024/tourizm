from django_filters import rest_framework as filters
from .models import Landmark, Tour

class LandmarkFilter(filters.FilterSet):
    class Meta:
        model = Landmark
        fields = {
            'name_landmark': ['exact'],
            'transport': ['exact'],
            'price': ['lt', 'gt'],
        }

class TourFilter(filters.FilterSet):
    class Meta:
        model = Tour
        fields = {
            'country': ['icontains'],
            'city': ['icontains'],
            'hotel': ['icontains'],
            'start_date': ['exact', 'lt', 'gt'],
            'end_date': ['exact', 'lt', 'gt'],
        }
