from django.contrib import admin
from .models import Teammate

class TeammateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_name', 'last_name')

admin.site.register(Teammate, TeammateAdmin)
