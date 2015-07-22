from core.models import Indicator
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.views.generic import TemplateView


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "mobile_index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        cursor = connection.cursor()
        cursor.execute("""SELECT indicator_id, AVG(value) as avg FROM core_indicatortotrackedtime
JOIN core_trackedtime ON core_indicatortotrackedtime.tracked_time_id = core_trackedtime.id
WHERE core_trackedtime.user_id = %s
GROUP BY indicator_id""", [self.request.user.pk])
        indicator_data = {}
        for indicator_id, avg_value in cursor.fetchall():
            indicator_data[indicator_id] = avg_value
        indicators = Indicator.objects.all()
        for indicator in indicators:
            if indicator.pk in indicator_data:
                indicator.avg_value = indicator_data[indicator.pk]
            else:
                indicator.avg_value = None
        context['indicators'] = indicators
        return context
