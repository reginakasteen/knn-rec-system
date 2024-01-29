from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'offer', 'rating_value', 'created_date',)
    search_fields = ('owner_name', 'offer',)
    list_editable = ('rating_value',)
