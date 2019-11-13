from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class ReserveForm(forms.Form):
    Nomrbre = forms.CharField(max_length=100)
    Desde = forms.DateField(widget=DateInput)
    Hasta = forms.DateField(widget=DateInput)
    