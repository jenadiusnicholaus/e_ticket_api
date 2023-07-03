from rest_framework import routers, serializers
from .models import *


class RouteOriginSerializers(serializers.ModelSerializer):

    class Meta:
        model = RouteOriginTable
        fields = '__all__'


class RouteDestinationSerializers(serializers.ModelSerializer):

    class Meta:
        model = RouteOriginTable
        fields = '__all__'


class BusInfosSerializers(serializers.ModelSerializer):
    route_destination = RouteDestinationSerializers()
    route_origin = RouteOriginSerializers()

    class Meta:
        model = BusInfosTable
        fields = '__all__'


class SeatsSerializers(serializers.ModelSerializer):
    bus = BusInfosSerializers()

    class Meta:
        model = SeatsTable
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):

    class Meta:
        model = BookingTable
        fields = '__all__'


class GetBookingSerializers(serializers.ModelSerializer):
    bus = BusInfosSerializers()
    seat = SeatsSerializers()

    class Meta:
        model = BookingTable
        fields = '__all__'


class PickUpPointsSerializers(serializers.ModelSerializer):

    class Meta:
        model = PickUpsTable
        fields = '__all__'


class DropPointsSerializers(serializers.ModelSerializer):

    class Meta:
        model = DropsTable
        fields = '__all__'


class BookingStateSerializers(serializers.ModelSerializer):
    booking = GetBookingSerializers()

    class Meta:
        model = BookingStateTable
        fields = '__all__'


class PostBookingStateSerializers(serializers.ModelSerializer):

    class Meta:
        model = BookingStateTable
        fields = '__all__'
