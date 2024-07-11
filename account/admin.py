from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        ("Personal details", {
            "fields": ("profile_picture","username","first_name","last_name","email","phone_number","password"),
        }),
        ("Account status", {
            "fields": ("professional_page",),
        }),
        ("Permissions", {
            "fields": ("is_active","is_staff","is_superuser","groups","user_permissions"),
        }),
        ("Important dates", {
            "fields": ("date_joined","last_login"),
        }),
    )
    
    list_display=['email','username','first_name','is_superuser']
    search_field ="email"


	
admin.site.register(CustomUser,CustomUserAdmin)









	