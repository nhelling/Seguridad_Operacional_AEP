from django.contrib import admin

from DERRAMES.models import Derrame

@admin.register(Derrame)

class DerrameAdmin(admin.ModelAdmin):
    list_display = ('fecha_derrame', 'posicion', 'sustancia', 'empresa', 'equipo','metros','pintura_afectada','juntas','estado')
    list_filter = ('posicion','sustancia', 'empresa','estado')
    search_fields= ('posicion','sustancia','empresa', 'estado',)
