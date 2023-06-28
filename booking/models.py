from django.db import models
from django.utils import timezone
import os


class RouteOriginTable(models.Model):
    name = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = '1. RouteOrigins'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name} '


class RouteDestinationTable(models.Model):
    name = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = '2. RouteDestination'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'


class BusInfosTable(models.Model):
    BUS_TYPE = (
        ('luxury', 'LUXURY'),
        ('semi-luxury', 'SEMI-LUXURY')
    )

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("bus_images", instance)
        return None

    bus_name = models.CharField(max_length=200, null=True, )
    bus_image = models.FileField(upload_to=image_upload_to, null=True)
    bus_id_number = models.CharField(max_length=200, null=True, )
    route_origin = models.ForeignKey(
        RouteOriginTable, on_delete=models.CASCADE, )

    route_destination = models.ForeignKey(
        RouteDestinationTable, on_delete=models.CASCADE, null=True
    )
    departure_date = models.DateField(default=timezone.now)
    departure_time = models.TimeField(default=timezone.now)
    fare = models.CharField(max_length=200, null=True)
    bus_type = models.CharField(max_length=200, null=True, choices=BUS_TYPE)

    class Meta:
        verbose_name = '3. Bus infos'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.bus_name}'


class SeatsTable(models.Model):
    SEAT_STATUS = ((0, "Available"), (1, "sold"))
    seat_number = models.CharField(max_length=100, null=True)
    status = models.IntegerField(
        max_length=200, null=True, choices=SEAT_STATUS)
    bus = models.ForeignKey(BusInfosTable, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '4. Seats'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.bus.bus_name} => seat number {self.seat_number}'


class BookingTable(models.Model):
    booked_by = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email_address = models.EmailField(max_length=20, null=True)
    amount_paid = models.CharField(max_length=13, null=True)
    bus = models.ForeignKey(BusInfosTable, on_delete=models.CASCADE, null=True)
    seat = models.ForeignKey(SeatsTable, on_delete=models.CASCADE, null=True)
    safari_day = models.DateField(default=timezone.now)
    pick_up = models.ForeignKey(
        "PickUpsTable", on_delete=models.CASCADE,  null=True)
    drop_point = models.ForeignKey(
        "DropsTable", on_delete=models.CASCADE,  null=True)

    class Meta:
        verbose_name = '4. Tickets'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self. booked_by} bus {self.bus.bus_name}  => seat number {self.seat.seat_number}'


class PickUpsTable(models.Model):
    name = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = '5. Pick Up points'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'


class DropsTable(models.Model):
    name = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = '6. Drop points '
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'
