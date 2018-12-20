from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_first_name', 'user_last_name', 'user_email', 'birth_date', 'year', 'phone', 'school',
	                'major', 'poc', 'gender', 'firstgen', 'trans', 'info', 'pronoun')
	change_list_template = 'chart.html'

	def user_first_name(self, instance):
		return instance.user.first_name

	def user_last_name(self, instance):
		return instance.user.last_name
	
	def user_email(self, instance):
		return instance.user.email

from .models import Survey

class SurveyAdmin(admin.ModelAdmin):
	list_display = ('reference', 'prior_attendee', 'suggestion', 'rating', 'comments', 'event_name')


#----------------------------------------------------------------------
#          Register the admin class with the associated model
#----------------------------------------------------------------------

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Survey, SurveyAdmin)
