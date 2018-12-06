from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from bridges.models import Survey
from bridges.models import Affiliate


@admin.register(Survey)
class SurveyAdmin(ImportExportModelAdmin):
	list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major','date')
# class SurveyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major')

# admin.site.register(Survey, SurveyAdmin)
@admin.register(Affiliate)
class Affiliate(ImportExportModelAdmin):
	list_display = ('name',)

from bridges.models import SaleSummary
@admin.register(SaleSummary)
class SaleSummaryAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major','date')
	change_list_template = 'chart.html'
	date_hierarchy = 'date'
	list_filter = ('name', 'email', 'phone', 'year', 'pronoun', 'dob', 'color', 'firstgen', 'workstudy', 'major','date')
        # response.context_data["summary"] = list(
        # 	qs
        #     .values(‘sale__category__name’)
        #     .annotate(**metrics)
        #     .order_by(‘-total_sales’)
        # )
        
