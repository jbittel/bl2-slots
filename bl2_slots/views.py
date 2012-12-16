from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

from bl2_slots.forms import RecordTorgueForm
from bl2_slots.mixins import JSONResponseMixin
from bl2_slots.models import RecordSlotsModel
from bl2_slots.models import MoxxiOutcomes
from bl2_slots.models import TorgueOutcomes


class PlayMoxxiView(TemplateView):
    template_name = 'bl2_slots/play_moxxi.html'

    def get_context_data(self, **kwargs):
        return {
            'params': kwargs,
            'outcomes': MoxxiOutcomes.objects.as_json()
        }

class PlayTorgueView(TemplateView):
    template_name = 'bl2_slots/play_torgue.html'

    def get_context_data(self, **kwargs):
        return {
            'params': kwargs,
            'outcomes': TorgueOutcomes.objects.as_json()
        }

class RecordTorgueCreateView(JSONResponseMixin, CreateView):
    form_class = RecordTorgueForm
    model = RecordSlotsModel
    success_url = reverse_lazy('record_torgue')

    def form_valid(self, form):
        """
        """
        self.object = form.save(request=self.request)

        if self.request.is_ajax():
            return self.render_json_response("success")
        else:
            return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        """
        if self.request.is_ajax():
            return self.render_json_response(form.errors, status=400)
        return super(RecordTorgueCreateView, self).form_invalid(form)
