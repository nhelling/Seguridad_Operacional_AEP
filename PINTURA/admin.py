from django.contrib import admin

from PINTURA.models import Pintura

@admin.register(Pintura)

class PinturaAdmin(admin.ModelAdmin):
    list_display = ('fecha_pos', 'posicion', 'lineas_de_guia', 'fecha_carteleria', 'carteleria', 'fecha_lineas_seguridad','lineas_seguridad','sector','pintado','estado')
    list_filter = ('posicion','fecha_pos', 'estado',)
    search_fields= ('posicion',)
