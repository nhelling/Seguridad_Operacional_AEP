from django.contrib import admin
from initial.models import Initial

@admin.register(Initial)
class InitialAdmin(admin.ModelAdmin):
    list_display = ['description','initial_image']
