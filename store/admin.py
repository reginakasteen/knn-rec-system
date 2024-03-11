from django.contrib import admin
from .models import Review, Owner, Offer, Category

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'offer', 'rating_value', 'created_date',)
    search_fields = ('owner_name', 'offer',)
    list_editable = ('rating_value',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'owned_by', 'category', 'period', 'room_type', 'rating', 'price',)
    prepopulated_fields = {'slug': ('name', 'owned_by')}
    search_fields = ('name', 'owned_by')
    list_editable = ('price', 'rating', 'period',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'location', 'rating', 'slug')
    prepopulated_fields = {'slug': ('owner_name',)}
    search_fields = ('owner_name', 'location',)
    list_editable = ('location', 'rating')
    list_filter = ()

