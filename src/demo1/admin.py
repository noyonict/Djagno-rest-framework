from django.contrib import admin
from .models import EmployeeInformation


class EmployeeInformationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'designation', 'team_name']
    list_display_links = ['name', 'email', 'designation', 'team_name']
    list_editable = ['phone']
    list_filter = ['team_name']
    search_fields = ['name', 'phone', 'email', 'designation', 'team_name']

    class Meta:
        model = EmployeeInformation


# Register your models here.
admin.site.register(EmployeeInformation, EmployeeInformationModelAdmin)
