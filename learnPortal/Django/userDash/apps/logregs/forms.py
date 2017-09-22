from django import forms

class Signin_Form(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=50)
    pw = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)

class Reg_Form(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=50)
    fname = forms.CharField(label="First Name", min_length=2)
    lname = forms.CharField(label="Last Name", min_length=2)
    pw = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)
    pwconfirm = forms.CharField(label="Password Confirmation", min_length=8, widget=forms.PasswordInput)
