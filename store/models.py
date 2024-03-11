from django.db import models
from account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from django.urls import reverse

PERIODS = [
    ("D", "per day"),
    ("W", "per week"),
    ("M", "per month"),
]

RATING = [
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('store:category_list_view', args=[self.slug])

    def __str__(self):
        return self.name

class Owner(models.Model):
    owner_name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, default=0)

    class Meta:
        verbose_name_plural = 'owners'
        ordering = ('owner_name',)

    def __str__(self):
        return self.owner_name


class Offer(models.Model):
    category = models.ForeignKey(Category, related_name='offer', on_delete=models.CASCADE)
    owned_by = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    rating = models.FloatField(null=True, default=0)

    period = models.CharField(max_length=10, choices=PERIODS, default='D')
    room_type = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'offers'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:offer_detail', args=[self.slug])

    def serialize(self):
        return {
            'id': self.pk,
            'category': self.category.name,
            'owned_by': self.owned_by.owner_name,
            'name': self.name,
            'slug': self.slug,
            'location': self.slug,
            'price': self.price,
            'is_available': self.is_available,
            'is_active': self.is_active,
            'period': self.period,
            'room_type': self.room_type,
            'picture': self.picture,
            'created': self.created,
            'description': self.description,

        }

    def __str__(self):
        return self.name


class Review(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_value = models.IntegerField(choices=RATING, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    review_text = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ('-created_date',)

    def __str__(self):
        return self.offer.name
