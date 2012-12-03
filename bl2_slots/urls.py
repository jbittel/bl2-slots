from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from bl2_slots.views import RecordTorgueCreateView


urlpatterns = patterns('',
    url(r'^record/$',
        TemplateView.as_view(template_name="bl2_slots/record.html"),
        name='record'),
    url(r'^record/torgue/$',
        RecordTorgueCreateView.as_view(),
        name='record_torgue'),
    url(r'^record/moxxi/$',
        TemplateView.as_view(template_name="bl2_slots/recordmoxximodel_form.html"),
        name='record_moxxi'),
)
