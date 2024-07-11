from django.contrib import admin
from App.models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display =['name','phone','email','gender','created_at']
    search_fields = ['name', 'gender','email','phone']
    list_per_page = 8



admin.site.register(Patient,PatientAdmin)
