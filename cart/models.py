from django.db import models
from store.models import Offer
from account.models import User


class Booking(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="booking")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    class Meta:
        ordering = ('-booking_date',)

