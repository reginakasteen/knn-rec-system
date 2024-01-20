from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User
from store.models import Category, Offer, Owner

class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'gender', 'is_admin', 'is_superuser', 'last_login',)
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    list_editable = ('gender', 'is_admin', 'is_superuser',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'owned_by', 'slug', 'room_type', 'is_active', 'is_available', 'price', 'location')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'owned_by')
    list_filter = ('is_available', 'is_active')
    list_editable = ('is_available', 'price')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'location', 'slug')
    prepopulated_fields = {'slug': ('owner_name',)}
    search_fields = ('owner_name', 'location',)
    list_filter = ()

