from django.contrib.humanize.templatetags.humanize import intcomma
from django.http import JsonResponse
from django.views.generic.base import TemplateView, View

from dsmr_datalogger.models.reading import DsmrReading
from dsmr_datalogger.models.statistics import MeterStatistics
from dsmr_datalogger.models.settings import DataloggerSettings
from dsmr_frontend.models.settings import FrontendSettings
from dsmr_stats.models.statistics import ElectricityStatistics
import dsmr_backend.services.backend


class Statistics(TemplateView):
    template_name = 'dsmr_frontend/statistics.html'

    def get_context_data(self, **kwargs):
        context_data = super(Statistics, self).get_context_data(**kwargs)
        context_data['capabilities'] = dsmr_backend.services.backend.get_capabilities()
        context_data['electricity_statistics'] = ElectricityStatistics.get_solo().export()
        context_data['frontend_settings'] = FrontendSettings.get_solo()

        try:
            latest_reading = DsmrReading.objects.all().order_by('-pk')[0]
        except IndexError:
            pass
        else:
            context_data['latest_reading'] = latest_reading
            context_data['delivered_sum'] = latest_reading.electricity_delivered_1 + \
                latest_reading.electricity_delivered_2
            context_data['returned_sum'] = latest_reading.electricity_returned_1 + \
                latest_reading.electricity_returned_2

        context_data['datalogger_settings'] = DataloggerSettings.get_solo()
        context_data['meter_statistics'] = MeterStatistics.get_solo()

        return context_data


class StatisticsXhrData(View):
    """ XHR view for fetching the dashboard header, displaying latest readings and price estimate, JSON response. """
    def get(self, request):
        return JsonResponse({
            'total_reading_count': intcomma(DsmrReading.objects.all().count()),
        })
