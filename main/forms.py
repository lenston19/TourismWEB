from django import forms
from functools import partial

DateInput1 = partial(forms.DateInput, {'class': 'datepicker Choice-hotel__date',
                                      'placeholder': 'Выберите дату заезда'})
DateInput2 = partial(forms.DateInput, {'class': 'datepicker Choice-hotel__date',
                                      'placeholder': 'Выберите дату отъезда'})

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput1())
    end_date = forms.DateField(widget=DateInput2())
