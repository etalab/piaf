from django.contrib import admin

from .models import User
from piaf.models import UserRelevancy


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_superuser",
        "is_certified",
        "level_completed",
        "paragraphs_count",
        "additional_answers_count",
        "date_joined",
        "is_active",
    )
    ordering = ("-date_joined",)
    list_filter = ("level_completed", "is_certified", "is_superuser", "is_active")
    search_fields = ("email", "is_superuser", "is_certified")
    list_editable = ("is_certified", "is_active")
    list_display_links = ("email",)
    fields = ("email", "is_staff", "is_certified", "level_completed")

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class Usercertification(User):
    class Meta:
        proxy = True


class UserAdmincertification(admin.ModelAdmin):
    list_display = ("email", "is_certified", "date_joined")
    ordering = ("email",)
    search_fields = ("email", "is_certified")
    list_editable = ("is_certified",)
    list_display_links = ("email",)
    fields = ("is_certified",)

    def get_queryset(self, request):
        return self.model.objects.filter(is_staff=False)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request, obj=None):
        return False

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


class UserRelevanciesAdmin(admin.ModelAdmin):
    list_display = ("user", "level", "score", "created_at")
    list_filter = ("user", "level", "score", "created_at")


admin.site.register(User, UserAdmin)
admin.site.register(Usercertification, UserAdmincertification)
admin.site.register(UserRelevancy, UserRelevanciesAdmin)
