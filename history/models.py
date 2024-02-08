from django.db import models
from account.models import User
from store.models import Offer

class ViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    view_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'views'

    def __int__(self):
        return self.vid
