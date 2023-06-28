from django.contrib import admin
from BSO.models import Bso

@admin.register(Bso)

class BsoAdmin(admin.ModelAdmin):
    list_display = ('fecha_bso','orden','titulo','pdf')
    list_filter = ('fecha_bso',)
    search_fields = ('fecha_bso','titulo')


