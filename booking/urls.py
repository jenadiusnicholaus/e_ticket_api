from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"buses", BusView)
router.register(r"seats", SeatsView)
router.register(r"make_booking", TicketsView)
router.register(r"get-booking-infos", GetBookingInfos)
router.register(r"get-pickup-points", PickUpPointsView)
router.register(r"get-drop-points", DropPointsView)
router.register(r"get-route-destionation-point", RouteDestinationView)
router.register(r"get-route-origin-point", RouteOriginView)
router.register(r"booking-state", BookingStateView)
router.register(r"get-origin-destination-routes", GetoriginRouteDestinationView)


urlpatterns = [
    path("", include(router.urls)),
]
