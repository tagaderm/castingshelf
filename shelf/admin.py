from django.contrib import admin
from shelf.models import *

# Register your models here.



# class BookAdmin(admin.ModelAdmin):
	
	



admin.site.register(Character)
admin.site.register(Actor)
admin.site.register(Book)
admin.site.register(Comment)