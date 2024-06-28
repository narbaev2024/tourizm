from django.contrib import admin
from .models import UserProfile, Landmark, Tour, Booking, Guide, GuideBookingStatus
from modeltranslation.admin import TranslationAdmin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'user',)


@admin.register(Landmark)
class LandmarkAdmin(TranslationAdmin):
    list_display = ('name_landmark', 'transport', 'price')
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'hotel', 'start_date', 'end_date', 'user')



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'landmark', 'hotel', 'restaurant', 'booking_date', 'status')


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(GuideBookingStatus)
class GuideBookingStatusAdmin(admin.ModelAdmin):
    list_display = ('guide', 'tour', 'status')


