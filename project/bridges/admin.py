from django.contrib import admin
from bridges.models import Survey

# Register your models here.


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'dob')

admin.site.register(Survey, SurveyAdmin)
