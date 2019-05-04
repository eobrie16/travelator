from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Search


class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('city','country', 'start_date', 'end_date')
        widgets = {
            'start_date': DatePickerInput(format='%Y-%m-%d'),
            'end_date': DatePickerInput(format='%Y-%m-%d'),
        }
    

