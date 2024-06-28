from django.urls import path
from .views import (
    UserProfileViewSet, LandmarkViewSet, TourViewSet,
    BookingViewSet, GuideViewSet, GuideBookingStatusViewSet
)

urlpatterns = [
    path('', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('<int:pk>/',UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='userprofile_detail'),
    path('landmark/', LandmarkViewSet.as_view({'get': 'list', 'post': 'create'}), name='landmark_list'),
    path('landmark/<int:pk>/', LandmarkViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='landmark_detail'),
    path('tour/', TourViewSet.as_view({'get': 'list', 'post': 'create'}), name='tour_list'),
    path('tour/<int:pk>/', TourViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='tour_detail'),
    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='booking_detail'),
    path('guide/', GuideViewSet.as_view({'get': 'list', 'post': 'create'}), name='guide_list'),
    path('guide/<int:pk>/', GuideViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='guide_detail'),
    path('guidebookingstatus/', GuideBookingStatusViewSet.as_view({'get': 'list', 'post': 'create'}),name='guidebookingstatus_list'),
    path('guidebookingstatus/<int:pk>/',GuideBookingStatusViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='guidebookingstatus_detail'),
]
