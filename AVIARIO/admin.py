from django.contrib import admin

from AVIARIO.models import Aviario

@admin.register(Aviario)

class AviarioAdmin(admin.ModelAdmin):
    list_display = ('fecha_aviario', 'especie_ave', 'empresa', 'equipo', 'estado')
    list_filter = ('especie_ave','empresa', 'estado',)
    search_fields= ('especie_ave','empresa', 'estado',)
