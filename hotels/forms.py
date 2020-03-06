from django import forms
from .models import Room


class CreateFrom(forms.Form):
    quantity = forms.ModelChoiceField(queryset=Room.objects.all(), to_field_name='quantity')


    def deploy(self, user):
        quantity = self.cleaned_data.get('quantity')

        deploy = Room(user=user, quantity=quantity)
        deploy.save()
        return deploy
