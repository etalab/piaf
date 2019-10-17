from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_superuser", "is_certified", "date_joined")
    ordering = ("email",)
    search_fields = ("email", "is_superuser", "is_certified")
    list_editable = ("is_superuser", "is_certified")
    list_display_links = ("email",)
    fields = ("email", "is_staff", "is_certified")


admin.site.register(User, UserAdmin)
