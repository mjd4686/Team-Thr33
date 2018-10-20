from django.contrib import admin
from bridges.models import Survey

# Register your models here.


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major')

admin.site.register(Survey, SurveyAdmin)
