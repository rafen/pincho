from django.views.generic.base import TemplateView
from button.models import Temp


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        temps = Temp.objects.all()
        context['latest_temp'] = temps[0]
        temps = list(temps[:200])
        temps.reverse()
        context['temps'] = temps
        return context
