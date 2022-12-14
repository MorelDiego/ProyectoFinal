from django import forms
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateContact(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=90)
    message = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'class': 'form-control-file'}))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
            ]
        help_text = {k: '' for k in fields}

class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]
        help_text = {k: '' for k in fields}

class AvatarForm(forms.Form):
    image = forms.ImageField()


