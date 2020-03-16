from django import forms
from .models import Room,Places, Hotels
from booking.models import Booking

""""
class CreateFrom(forms.Form):
    quantity = forms.ModelChoiceField(queryset=Room.objects.all(), to_field_name='quantity')
    def deploy(self, user):
        quantity = self.cleaned_data.get('quantity')
        deploy = Room(user=user, quantity=quantity)
        deploy.save()
        return deploy
"""
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

###### Place Add Form
class PlacesForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Place Name'}))
    country = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Country Name'}))


    def clean(self):
        name = self.cleaned_data.get('name')
        country = self.cleaned_data.get('country')

        if len(name) <1:
            raise forms.ValidationError('Enter place name!')
        else:
            if len(country) <1:
                raise forms.ValidationError('Enter country name!')


    class Meta:
        model = Places
        fields = [
            'name',
            'country',
            'image',
        ]


# ======================= Hotel Add Form ======================
# Place choice field add kora hoy nai
class HotelsAddForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Hotel Name'}))

    address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    city = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    telephone = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))

    def clean(self):
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        telephone = self.cleaned_data.get('telephone')



        if len(name) <1:
            raise forms.ValidationError('Enter hotel name')
        else:
            if len(address) <1:
                raise forms.ValidationError('Enter address')
            else:
                if len(telephone) <1:
                    raise forms.ValidationError('Enter mobile number')



    class Meta:
        model = Hotels
        fields = [
            'name',
            'places',
            'address',
            'image',
            'city',
            'telephone',
            'description',
            'rating',

        ]



class HotelsAddFormAdmin(forms.ModelForm):

    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Hotel Name'}))

    address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    city = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    telephone = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))

    def clean(self):
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        telephone = self.cleaned_data.get('telephone')



        if len(name) <1:
            raise forms.ValidationError('Enter hotel name')
        else:
            if len(address) <1:
                raise forms.ValidationError('Enter address')
            else:
                if len(telephone) <1:
                    raise forms.ValidationError('Enter mobile number')


    class Meta:
        model = Hotels
        fields = [
            'name',
            'places',
            'user',
            'address',
            'image',
            'city',
            'telephone',
            'description',
            'rating',
            'draft',
        ]







class RoomAddForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Room name'}))
    roomtype = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Room type'}))
    capacity = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Capacity'}))
    price = forms.FloatField(required=False)
    quantity = forms.IntegerField(required=False)
    discount = forms.FloatField(required=False)
    vat = forms.FloatField(required=False)
    service_charge = forms.FloatField(required=False)



    def clean(self):
        name = self.cleaned_data.get('name')


        if len(name) < 1:
            raise forms.ValidationError('Enter room name')






    class Meta:
        model = Room

        fields = [
            'name',
            'hotel',
            'roomtype',
            'image',
            'capacity',
            'price',
            'quantity',
            'discount',
            'vat',
            'service_charge',
        ]

