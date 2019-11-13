from django import forms
from .models import RentForm
from django.forms import DateTimeField
from django.contrib.admin import widgets

class ReserveForm(forms.ModelForm):

    event_date = DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])

    class Meta:
        model = RentForm
        fields = ('Nombre', 'Desde','Hasta',)

        def __init__(self, *args, **kwargs):
            super(RentForm, self).__init__(*args, **kwargs)
            self.fields['event_date'].widget = widgets.AdminSplitDateTime()