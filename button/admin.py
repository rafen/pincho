from django.contrib import admin
from button.models import ChairState, Temp


class SitStateAdmin(admin.ModelAdmin):
    list_display = ('in_use', 'acc', 'created')
    list_filter = ['created']


class TempAdmin(admin.ModelAdmin):
    list_display = ('temp', 'humidity', 'created')
    list_filter = ['created']

admin.site.register(ChairState, SitStateAdmin)
admin.site.register(Temp, TempAdmin)
