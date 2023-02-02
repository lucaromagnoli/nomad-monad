from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class ContactForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 300px;",
                "placeholder": "subject",
            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 300px;",
                "placeholder": "name",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "style": "max-width: 300px;",
                "placeholder": "email",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "style": "max-width: 300px;",
                "placeholder": "message",
            }
        )
    )
