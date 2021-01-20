from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('email', 'username','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = 'Email Address'
        self.fields['username'].label = 'Display Name'

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password',
                  'is_staff', 'is_active')

    def clean_password(self):
        return self.initial["password"]
