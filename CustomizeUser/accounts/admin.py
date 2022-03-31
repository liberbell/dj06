from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from .models import Students, Schools

# Register your models here.
User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("username", "email", "is_staff")
    fieldsets = (
        ("User Info", {'fields': ("username", "email", "password", "website", "picture")}),
        ("Permission Group", {'fields': ("is_staff", "is_active", "is_superuser")}),
    )

    add_fieldsets = (
        ("User Info", {'fields': ("username", "email", "password", "confirm_password")
        }),
    )

admin.site.register(User, CustomizeUserAdmin)
admin.site.register(Students)
admin.site.register(Schools)