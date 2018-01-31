from django.contrib import admin

from .models import Consulta, Opcio, Invitacio, Vot

class ChoiceInLine(admin.StackedInline):
	model = Opcio
	extra = 2

class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('titul', 'user', 'finici', 'ffinal')
	inlines = [ChoiceInLine]

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)

class OpcioAdmin(admin.ModelAdmin):
	list_display = ('consulta', 'text', 'vots')

	def get_queryset(self, request):
		qs = Opcio.objects.all()
		super().get_queryset(request)
		if request.user.is_superuser:
			return qs	
		return qs.filter(consulta__user=request.user)


admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Opcio, OpcioAdmin)
admin.site.register(Invitacio)
admin.site.register(Vot)
	