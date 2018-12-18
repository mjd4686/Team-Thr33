from django.contrib import admin


from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
	list_display = ( 'user', 'birth_date',)
	change_list_template = 'chart.html'
	date_hierarchy = 'birth_date'


from .models import Event
class EventAdmin(admin.ModelAdmin):
	list_display = ('name',)


#----------------------------------------------------------------------
#          Register the admin class with the associated model
#----------------------------------------------------------------------

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event, EventAdmin)
