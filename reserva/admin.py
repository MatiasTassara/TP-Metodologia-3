from django.contrib import admin

# Register your models here.
from reserva.models import City, RealState, Reservation, RentDate

admin.site.register(City)
admin.site.register(RealState)
admin.site.register(Reservation)
admin.site.register(RentDate)