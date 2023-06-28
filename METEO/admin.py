from django.contrib import admin
from METEO.models import Meteorologia

@admin.register(Meteorologia)

class MeteorologiaAdmin(admin.ModelAdmin):
    list_display = ('meteorologia',)
    list_filter = ('meteorologia',)
    search_fields = ('meteorologia',)
