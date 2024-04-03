from django.contrib import admin

from . import models

# Models
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(models.Users, UsersAdmin)