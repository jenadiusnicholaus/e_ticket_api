from rest_framework import viewsets
from .serializers import *
from .models import BusInfosTable
from rest_framework.response import Response
from rest_framework import viewsets, status


class BookingStateView(viewsets.ModelViewSet):
    queryset = BookingStateTable.objects.all()
    serializer_class = BookingStateSerializers
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        _booking_id = request.query_params.get("booking_id", None)

        try:
            q = BookingStateTable.objects.get(booking_id=_booking_id)
            serializer = self.get_serializer(q)

            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"booking_state": serializer.data},
            }
            return Response(data=response_obj)
        except:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
            }
            return Response(data=response_obj)

    def put(self, request, *args, **kwargs):
        _booking_id = request.query_params.get("booking_id")

        _state = request.query_params.get("state")

        instance = self.get_queryset().get(
            booking_id=_booking_id,
        )
        data = {
            "state": _state,
        }
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "Record updated successfully",
                "data": {"state": serializer.data},
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Failed to update",
            }
            Response(response_obj)


class RouteOriginView(viewsets.ModelViewSet):
    queryset = RouteOriginTable.objects.all()
    serializer_class = RouteOriginSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"routes": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"errors_massage": serializer.data},
            }
            return Response(data=response_obj)


class RouteDestinationView(viewsets.ModelViewSet):
    queryset = RouteDestinationTable.objects.all()
    serializer_class = RouteDestinationSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"routes": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"errors_massage": serializer.data},
            }
            return Response(data=response_obj)


class BusView(viewsets.ModelViewSet):
    queryset = BusInfosTable.objects.all()
    serializer_class = BusInfosSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        _route_origin_id = request.query_params.get("route_origin", None)
        _route_destination_id = request.query_params.get("route_destination", None)
        _route_destination_id = request.query_params.get("route_destination", None)

        _departure_date = request.query_params.get("departure_date", None)

        if _route_origin_id and _route_origin_id:
            queryset = queryset.filter(
                route_origin=_route_origin_id,
                route_destination=_route_destination_id,
                departure_date=_departure_date,
            )

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"buses": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"errors_massage": serializer.data},
            }
            return Response(data=response_obj)


class SeatsView(viewsets.ModelViewSet):
    queryset = SeatsTable.objects.all()
    serializer_class = SeatsSerializers
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        _bus_id = request.query_params.get("bus_id", None)

        if _bus_id:
            queryset = queryset.filter(bus=_bus_id)

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"seats": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"error_messages": serializer.data},
            }
            return Response(data=response_obj)

    def put(self, request, *args, **kwargs):
        bus_id = request.query_params.get("bus_id")

        _seat_id = request.query_params.get("seat_id")

        instance = self.get_queryset().get(
            bus__id=bus_id,
            id=_seat_id,
        )
        data = {
            "status": 1,
        }
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            response_obj = {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "Record updated successfully",
                "data": {"selected_seat_infos": serializer.data},
            }
            return Response(response_obj)
        else:
            response_obj = {
                "success": False,
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Failed to update",
            }
            Response(response_obj)


class GetBookingInfos(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = GetBookingSerializers
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        _booking_id = request.query_params.get("booking_id", None)

        if _booking_id:
            queryset = queryset.filter(id=_booking_id)

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"booking_info": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"message": serializer.data},
            }
            return Response(data=response_obj)


class TicketsView(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializers
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        _booking_id = request.query_params.get("booking_id", None)

        if _booking_id:
            queryset = queryset.filter(id=_booking_id)

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"booking_infos": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"booking_infos": serializer.data},
            }
            return Response(data=response_obj)

    def create(self, request, *args, **kwargs):
        booked_by = request.data.get("full_name")
        phone_numner = request.data.get("phone_number")
        email_address = request.data.get("email_address")
        amount_paid = request.data.get("amount_paid")
        bus_id = request.data.get("bus_id")
        seat_id = request.data.get("seat_id")
        pick_up_point = request.data.get("pickup_point_id")
        drop_point = request.data.get("drop_point_id")
        safari_day = request.data.get("safari_day")

        data = {
            "booked_by": booked_by,
            "phone_number": phone_numner,
            "email_address": email_address,
            "amount_paid": amount_paid,
            "bus": bus_id,
            "seat": seat_id,
            "pick_up": pick_up_point,
            "drop_point": drop_point,
            "safari_day": safari_day,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_obj = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "Booking is made successfully",
            "headers": headers,
            "data": {"booking_info": serializer.data},
        }
        return Response(response_obj)


class PickUpPointsView(viewsets.ModelViewSet):
    queryset = PickUpsTable.objects.all()
    serializer_class = PickUpPointsSerializers
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        _pickup_point_id = request.query_params.get("pickup_point_id", None)

        if _pickup_point_id:
            queryset = queryset.filter(id=_pickup_point_id)

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"drop_points": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"error_message": serializer.data},
            }
            return Response(data=response_obj)


class DropPointsView(viewsets.ModelViewSet):
    queryset = DropsTable.objects.all()
    serializer_class = DropPointsSerializers
    authentication_classes = []
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        _pickup_point_id = request.query_params.get("drop_point_id", None)

        if _pickup_point_id:
            queryset = queryset.filter(id=_pickup_point_id)

        serializer = self.get_serializer(queryset, many=True)

        if queryset.exists():
            response_obj = {
                "success": True,
                "status_code": status.HTTP_200_OK,
                "message": "Found",
                "data": {"pick_up_points": serializer.data},
            }
            return Response(data=response_obj)
        else:
            response_obj = {
                "success": False,
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Not Found",
                "data": {"error_message": serializer.data},
            }
            return Response(data=response_obj)
