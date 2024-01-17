from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'gender', 'is_admin', 'last_login')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)