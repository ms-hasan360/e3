from django import forms


class UserForm(forms.Form):
    user_name = forms.CharField()
    user_email = forms.EmailField()