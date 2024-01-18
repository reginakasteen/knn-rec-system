from django.db import models
from account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.s])

    def __str__(self):
        return self.name

class Owner(models.Model):
    owner_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(null=True)


class Offer(models.Model):
    category = models.ForeignKey(Category, related_name='offer', on_delete=models.CASCADE)
    owned_by = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    rating = models.FloatField(null=True)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    room_type = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'offers'
        ordering = ('-created',)

        def __str__(self):
            return self.name