from django.contrib import admin


from .models import People
class PeopleAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'dob',)


from .models import Event
class EventAdmin(admin.ModelAdmin):
	list_display = ('name',)




#----------------------------------------------------------------------
#          Register the admin class with the associated model
#----------------------------------------------------------------------

admin.site.register(People, PeopleAdmin)
admin.site.register(Event, EventAdmin)
