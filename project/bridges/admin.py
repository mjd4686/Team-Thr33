from django.contrib import admin


from .models import People
class PeopleAdmin(admin.ModelAdmin):
	list_display = ( 'email','name', 'phone', 'school',  'dob', 'major', 'poc', 'gender', 'role')
	change_list_template = 'chart.html'
	date_hierarchy = 'dob'


from .models import Event
class EventAdmin(admin.ModelAdmin):
	list_display = ('name',)




#----------------------------------------------------------------------
#          Register the admin class with the associated model
#----------------------------------------------------------------------

admin.site.register(People, PeopleAdmin)
admin.site.register(Event, EventAdmin)
