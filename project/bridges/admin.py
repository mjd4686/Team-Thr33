from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from bridges.models import Survey
from bridges.models import Affiliate


@admin.register(Survey)
class SurveyAdmin(ImportExportModelAdmin):
	list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major')
# class SurveyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major')

# admin.site.register(Survey, SurveyAdmin)
@admin.register(Affiliate)
class Affiliate(ImportExportModelAdmin):
	list_display = ('name',)
