from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email", "first_name", "last_name", "age", "is_active"]
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (('Personal Info'), {'fields': ('first_name', 'last_name', 'email', 'age')}),
    #     (('Activation Info'), {'fields': ("activationKey", "activationExpires", )}),
    #     (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                    'groups', 'user_permissions')}),
    #     (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
