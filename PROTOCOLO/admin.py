from django.contrib import admin
from PROTOCOLO.models import Protocolo

@admin.register(Protocolo)

class BsoAdmin(admin.ModelAdmin):
    list_display = ('fecha_protocolo','orden','titulo','pdf')
    list_filter = ('fecha_protocolo',)
    search_fields = ('fecha_protocolo','titulo')
