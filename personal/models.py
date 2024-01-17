from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator, URLValidator




















# class Offer(models.Model):
#     offer_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     hotel_name = models.CharField(max_length=50)
#     location = models.CharField(max_length=20)
#     price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
#     rating = models.FloatField(null=True)
#     is_available = models.BooleanField(default=True)
#     room_type = models.CharField(max_length=30)
#     picture = models.CharField(null=True)
#     description = models.TextField(null=True)
#
#
#     def __str__(self):
#         return  f"{self.offer_id} - {self.name} - {self.is_available} - {self.price} - {self.rating}"
#
#
# class BaseInteraction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
#
#     class Meta:
#         abstract = True
#
#
# class Booking(BaseInteraction):
#     booking_id = models.AutoField(primary_key=True)
#     booking_date = models.DateTimeField(auto_now_add=True)
#     checkin_date = models.DateTimeField(auto_now=False, auto_now_add=False)
#     checkout_date = models.DateTimeField(auto_now=False, auto_now_add=False)
#
#     def clean(self):
#         if self.checkin_date >= self.checkout_date:
#             raise ValidationError("Checkin date should be before checkout date.")
#
#     def __str__(self):
#         return  f"{self.booking_id} - {self.user_id} - {self.offer_id} - {self.booking_date}"
#
# class ViewHistory(BaseInteraction):
#     view_id = models.AutoField(primary_key=True)
#     view_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return  f"{self.view_id} - {self.user_id} - {self.offer_id} - {self.view_date}"
#
# class Review(BaseInteraction):
#     review_id = models.AutoField(primary_key=True)
#     review_date = models.DateTimeField(auto_now_add=True)
#     rating_value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
#     review_text = models.TextField(null=True)
#     changed =  models.BooleanField(default=False)
#
#     def __str__(self):
#         return  f"{self.review_id} - {self.user_id} - {self.offer_id} - {self.review_date} - {self.rating_value}"
