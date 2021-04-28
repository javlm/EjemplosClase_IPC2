from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    remember = forms.BooleanField(label="exampleCheck1", required=False)

class RegisterForm(forms.Form):
    name = forms.CharField(label="name")
    lastname = forms.CharField(label="lastname")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    username = forms.CharField(label="username")
    #area = forms.CharField(widget=forms.TextAreaField())
