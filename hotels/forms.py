from django import forms
from .models import Room
from booking.models import Booking

class CreateFrom(forms.Form):
    quantity = forms.ModelChoiceField(queryset=Room.objects.all(), to_field_name='quantity')


    def deploy(self, user):
        quantity = self.cleaned_data.get('quantity')

        deploy = Room(user=user, quantity=quantity)
        deploy.save()
        return deploy



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =( 'checkin', 'checkout' )

        widgets = {
            'checkin': forms.DateInput(attrs={'class': 'datepicker'}),
            'checkout': forms.DateInput(attrs={'class': 'datepicker'})
        }

