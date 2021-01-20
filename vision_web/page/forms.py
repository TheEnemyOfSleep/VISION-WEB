from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
        'type': "text",
        'name': "Name",
        'class': "t-input js-tilda-rule",
        'placeholder': "Имя",
        'data-tilda-rule': "name",
        'style': """color:#181818;
                    border:1px solid #c9c9c9;
                    background-color:#ededed;
                    border-radius: 0px;
                    -moz-border-radius: 0px;
                    -webkit-border-radius: 0px;"""
        }),
        label=''
        )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
        'type': "tel",
        'class': "t-input mask-phone",
        'placeholder': "Телефон",
        'style': """color:#181818;
                    border:1px
                    solid #c9c9c9;
                    background-color:#ededed;
                    border-radius: 0px;
                    -moz-border-radius: 0px;
                    -webkit-border-radius: 0px;"""
        }),
        label='')

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        phone = cleaned_data.get('phone')
        if not name and not phone:
            raise forms.ValidationError('You have to write something!')