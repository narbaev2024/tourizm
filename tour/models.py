from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=32)

    def __str__(self):
        return self.nickname


class Landmark(models.Model):
    CHOICES_TRANSPORT = (
        ("Автобус", "Автобус"),
        ("Маршрутка", "Маршрутка"),
        ("Такси", "Такси")
    )

    name_landmark = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    transport = models.CharField(max_length=32, choices=CHOICES_TRANSPORT)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name_landmark


class Tour(models.Model):
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    hotel = models.CharField(max_length=32)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bookings')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    landmark = models.ForeignKey(Landmark, on_delete=models.CASCADE, related_name='bookings')
    hotel = models.CharField(max_length=32)
    restaurant = models.CharField(max_length=32)
    booking_date = models.DateField()
    CHOICES_STATUS = (
        ("Бронировано", "Бронировано"),
        ("Ожидание", "Ожидание"),
        ("Отменено", "Отменено"),
        ("Подтверждено", "Подтверждено"),
    )
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default='Ожидание')



class Guide(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='guide_profile')
    excursions = models.ManyToManyField(Landmark, related_name='guides')
    tours = models.ManyToManyField(Tour, related_name='guides')

    def __str__(self):
        return self.user.nickname


class GuideBookingStatus(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    CHOICES_BOOKING_STATUS = (
        ("Подтверждено", "Подтверждено"),
        ("Отказ", "Отказ"),
        ("Изменение", "Изменение")
    )
    status = models.CharField(max_length=20, choices=CHOICES_BOOKING_STATUS)

