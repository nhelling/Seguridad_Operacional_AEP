from django.contrib import admin
from ADR.models import Adr

@admin.register(Adr)

class AdrAdmin(admin.ModelAdmin):
    list_display = ('fecha_presentado','titulo','fecha_aprobado','estado','archivo')
    list_filter = ('fecha_presentado','titulo','fecha_aprobado','estado')
    search_fields = ('estado','titulo')
