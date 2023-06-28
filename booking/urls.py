from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'search-bus', BusView)
router.register(r'seats', SeatsView)
router.register(r'make_booking', TicketsView)
router.register(r'get-booking-infos', GetBookingInfos)
router.register(r'get-pickup-points', PickUpPointsView)
router.register(r'get-drop-points', DropPointsView)


urlpatterns = [
    path('', include(router.urls)),
]
