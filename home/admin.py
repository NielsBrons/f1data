from django.contrib import admin
from django import forms
from .models import Races, Events, Circuit

class RacesAdminForm(forms.ModelForm):

    class Meta:
        model = Races
        fields = '__all__'


class RacesAdmin(admin.ModelAdmin):
    form = RacesAdminForm
    list_display = ['name', 'created', 'last_updated', 'season', 'round', 'circuit']
    readonly_fields = ['name', 'created', 'last_updated', 'season', 'round', 'circuit']

admin.site.register(Races, RacesAdmin)


class EventsAdminForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = '__all__'


class EventsAdmin(admin.ModelAdmin):
    form = EventsAdminForm
    list_display = ['created', 'last_updated', 'date', 'time', 'type']
    readonly_fields = ['created', 'last_updated', 'date', 'time', 'type']

admin.site.register(Events, EventsAdmin)


class CircuitAdminForm(forms.ModelForm):

    class Meta:
        model = Circuit
        fields = '__all__'


class CircuitAdmin(admin.ModelAdmin):
    form = CircuitAdminForm
    list_display = ['name', 'created', 'last_updated', 'country']
    readonly_fields = ['name', 'created', 'last_updated', 'country']

admin.site.register(Circuit, CircuitAdmin)