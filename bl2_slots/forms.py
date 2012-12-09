from django.forms import ModelForm
from django.forms import RadioSelect

from bl2_slots.models import RecordSlotsModel


class RecordTorgueForm(ModelForm):
    class Meta:
        model = RecordSlotsModel
        fields = ('sa', 'sb', 'sc')
        widgets = {
            'sa': RadioSelect,
            'sb': RadioSelect,
            'sc': RadioSelect,
        }

    def save(self, commit=True, *args, **kwargs):
        form = super(RecordTorgueForm, self).save(commit=False)
        request = kwargs.pop('request', None)

        form.slots_type = 'T'

        if request:
            form.client_ip = request.META['REMOTE_ADDR']

        if commit:
            form.save()
        return form
