from django import forms

class msg_form(forms.Form):
    msg = forms.CharField(label='', widget=forms.Textarea)
