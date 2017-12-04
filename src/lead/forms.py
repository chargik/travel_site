from django import forms

from .models import Join
from .validators import validate_telephone

class JoinForm(forms.ModelForm):
    lead_name = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class':'form-control'}
            ))
    telephone = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваш телефон', 'class':'form-control', 'type':'tel'}
            ), validators=[validate_telephone])
    # email = forms.EmailField(label='',
    #     widget=forms.EmailInput(
    #         attrs={'placeholder':'Ваш email','class':'form-control'}
    #         ))

    class Meta:
        model = Join
        fields = ['lead_name', 'telephone']#, 'email']
