from django.contrib import admin
from . models import *

admin.site.register(RouteDestinationTable)
admin.site.register(RouteOriginTable)
admin.site.register(BusInfosTable)
admin.site.register(SeatsTable)
admin.site.register(BookingTable)
admin.site.register(PickUpsTable)
admin.site.register(DropsTable)
