from django.contrib import admin
from history.models import ViewHistory

@admin.register(ViewHistory)

class ViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'offer', 'view_date',)
    search_fields = ('user', 'offer',)
