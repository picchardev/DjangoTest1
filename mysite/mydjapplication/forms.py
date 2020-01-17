from django import forms


class RegistrationForm(forms.Form):
    user_id = forms.CharField(max_length=20)
    user_pass = forms.CharField(max_length=10)
