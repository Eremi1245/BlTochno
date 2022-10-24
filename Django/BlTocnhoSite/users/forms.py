from django import forms

from users.models import BlTochnoUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = BlTochnoUser
        fields = ['username','first_name','last_name','email','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = BlTochnoUser
        fields = ['username','password']


class PasswordRecoveryForm(forms.ModelForm):
    class Meta:
        model = BlTochnoUser
        fields = '__all__'