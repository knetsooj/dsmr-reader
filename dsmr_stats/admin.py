from django.contrib import admin
from django.forms import widgets
from django.db import models
from solo.admin import SingletonModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models.note import Note
from .models.statistics import HourStatistics, DayStatistics, ElectricityStatistics


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('day', 'description')
    formfield_overrides = {
        models.CharField: {'widget': widgets.Textarea},
    }

    def get_form(self, request, obj=None, **kwargs):
        form = super(NoteAdmin, self).get_form(request, obj, **kwargs)
        day = request.GET.get('day')

        if day:
            form.base_fields['day'].initial = day

        return form


@admin.register(DayStatistics)
class DayStatisticsAdmin(admin.ModelAdmin):
    actions = None
    ordering = ['-day', 'total_cost']
    list_display = ('day', 'electricity_merged', 'electricity_returned_merged', 'total_cost')
    list_filter = (
        ('day', DateRangeFilter),
    )


@admin.register(HourStatistics)
class HourStatisticsAdmin(admin.ModelAdmin):
    actions = None
    ordering = ['-hour_start']
    list_display = ('hour_start', 'electricity_merged', 'electricity_returned_merged')
    list_filter = (
        ('hour_start', DateTimeRangeFilter),
    )


@admin.register(ElectricityStatistics)
class ElectricityStatisticsAdmin(SingletonModelAdmin):
    actions = None
