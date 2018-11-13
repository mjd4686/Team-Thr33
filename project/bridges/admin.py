from django.contrib import admin
from bridges.models import Survey
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Survey)
class SurveyAdmin(ImportExportModelAdmin):
	list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major')
# class SurveyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major')

# admin.site.register(Survey, SurveyAdmin)
