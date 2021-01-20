from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Pasword'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't mach"))
        return password2


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password',
                  'is_staff', 'is_active')

    def clean_password(self):
        return self.initial["password"]
