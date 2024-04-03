from django.contrib import admin

from . import models

# Models
class Buses(admin.ModelAdmin):
    list_display = ('bus_name',)

admin.site.register(models.Bus, Buses)

class Booking(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(models.Book, Booking)