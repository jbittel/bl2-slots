from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from bl2_slots.views import RecordTorgueCreateView
from bl2_slots.views import PlayMoxxiView
from bl2_slots.views import PlayTorgueView


urlpatterns = patterns('',
    url(r'^record/$',
        TemplateView.as_view(template_name="bl2_slots/record.html"),
        name='record'),
    url(r'^record/moxxi/$',
        TemplateView.as_view(template_name="bl2_slots/recordmoxximodel_form.html"),
        name='record_moxxi'),
    url(r'^record/torgue/$',
        RecordTorgueCreateView.as_view(),
        name='record_torgue'),
    url(r'^play/moxxi/$',
        PlayMoxxiView.as_view(),
        name='play_moxxi'),
    url(r'^play/torgue/$',
        PlayTorgueView.as_view(),
        name='play_torgue'),
)
