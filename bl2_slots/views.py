from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.utils import simplejson as json
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from bl2_slots.forms import RecordTorgueForm
from bl2_slots.models import RecordTorgueModel
from bl2_slots.mixins import JSONResponseMixin


class RecordTorgueCreateView(JSONResponseMixin, CreateView):
    form_class = RecordTorgueForm
    model = RecordTorgueModel
    success_url = reverse_lazy('record_torgue')

    def form_valid(self, form):
        """
        """
        if self.request.is_ajax():
            self.object = form.save()
            return self.render_json_response("success")
        return super(RecordTorgueCreateView, self).form_valid(form)

    def form_invalid(self, form):
        """
        """
        if self.request.is_ajax():
            return self.render_json_response(form.errors, status=400)
        return super(RecordTorgueCreateView, self).form_invalid(form)
