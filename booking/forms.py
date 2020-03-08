from django import forms
from .models import *
"""
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =( 'checkin', 'checkout' )

        widgets = {
            'checkin': forms.DateInput(attrs={'class': 'datepicker'}),
            'checkout': forms.DateInput(attrs={'class': 'datepicker'})
        }
"""
