from django.forms import ModelForm
from django.forms import RadioSelect

from bl2_slots.models import RecordTorgueModel


class RecordTorgueForm(ModelForm):
    class Meta:
        model = RecordTorgueModel
        fields = ('sa', 'sb', 'sc')
        widgets = {
                'sa': RadioSelect,
                'sb': RadioSelect,
                'sc': RadioSelect,
        }

#    def clean(self):
#        cleaned_data = super(RecordTorgueForm, self).clean()
        # TODO insert client IP address
#        return cleaned_data 
