from django import forms
from .models import Contact




class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=55, required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    subject = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control',}))
    message = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'class': 'form-control md-textarea',}))

    class Meta:
            model = Contact
            fields = [
                'name', 'email', 'subject', 'message'
            ]

class ReplyMessage(forms.ModelForm):
    reply = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'class': 'form-control md-textarea'}))

    class Meta:
        model = Contact
        fields = [
            'reply',
        ]



class SendMessage(forms.ModelForm):
    message = forms.CharField(max_length=500, required=False, widget=forms.TextInput(
				attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Type a message'}))

    class Meta:
        model = Contact
        fields = [
            'message',
        ]
