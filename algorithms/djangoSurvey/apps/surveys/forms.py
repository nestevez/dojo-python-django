from django import forms

class Survey1(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    birthday = forms.DateField(label='Birthday')
    email = forms.EmailField(label='Email', min_length=5, max_length=100)
    password = forms.CharField(label='Password')
