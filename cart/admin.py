from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'offer', 'booking_date', 'checkin_date', 'checkout_date',)
    search_fields = ('user', 'offer',)
    list_editable = ('checkin_date', 'checkout_date',)