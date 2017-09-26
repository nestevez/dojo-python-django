from django import forms

class msg_form(forms.Form):
    msg = forms.CharField(label='', widget=forms.Textarea)

class edit_user(forms.Form):
    email = forms.EmailField(label="Email Address")
    fname = forms.CharField(label="First Name", min_length=2)
    lname = forms.CharField(label="Last Name", min_length=2)

class edit_pw(forms.Form):
    pw = forms.CharField(label="Password", min_length=8)
    cpw = forms.CharField(label="Password Confirmation")
