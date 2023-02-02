from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class ContactForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 300px;",
                "placeholder": "Email",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 300px;",
                "placeholder": "Email",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "style": "max-width: 300px;",
                "placeholder": "Message",
            }
        )
    )
