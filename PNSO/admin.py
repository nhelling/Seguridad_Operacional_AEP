from django.contrib import admin

from PNSO.models import Pnso

@admin.register(Pnso)

class PnsoAdmin(admin.ModelAdmin):
    list_display = ('nro', 'fecha_recibido', 'fecha_evento', 'texto', 'fecha_respuesta', 'estado','mitigacion','cierre')
    list_filter = ('nro','fecha_recibido', 'fecha_evento','estado',)
    search_fields= ('nro',)

