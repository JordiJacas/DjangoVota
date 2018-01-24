from django.contrib import admin

from .models import Consulta, Opcio, Invitacio, Vot

class ConsultaAdmin(admin.ModelAdmin):
    flist_display = ('titul', 'text', 'user', 'dinicial', 'ffinal')



admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Opcio)
admin.site.register(Invitacio)
admin.site.register(Vot)
