from django.contrib import admin

from SMS.models import Sms

@admin.register(Sms)

class PnsoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'evento', 'descripcion', 'mitigacion', 'estado', 'status','seguimiento','image_sms')
    list_filter = ('fecha','evento', 'estado','status',)
    search_fields= ('fecha','evento')
