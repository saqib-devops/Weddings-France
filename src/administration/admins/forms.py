from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div
from django import forms

from .models import GuestGroup, Guest, Provider, InvitationLetter, Table


class Row(Div):
    css_class = "row"


class GuestGroupMetaForm(forms.ModelForm):
    class Meta:
        model = GuestGroup
        fields = ('group_name',)
        widgets = {
            'group_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class GuestMetaForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('group', 'guest_name')
        widgets = {
            'guest_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].widget.attrs.update({"class": "form-control"})


class ProviderMetaForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ('provider_name', 'service', 'email', 'phone_number',
                  'total_cost', 'paid', 'attachment', 'comment')
        widgets = {
            'provider_name': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'total_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'paid': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attachment'].widget.attrs.update({"class": "form-control"})
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('provider_name', css_class='form-group col-sm-4 '),
                Column('service', css_class=' col-sm-4 '),
                Column('phone_number', css_class='form-group col-sm-4 '),
                Column('email', css_class='form-group col-sm-6 '),
                Column('total_cost', css_class='form-group col-sm-3 '),
                Column('paid', css_class='form-group col-sm-3 '),
                Column('attachment', css_class='form-group col-sm-12 '),
                Column('comment', css_class='col-sm-12 '),

            ),

        )


class InvitationForm(forms.ModelForm):
    class Meta:
        model = InvitationLetter
        fields = ('total_invitation',)
        widgets = {
            'total_invitation': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('table_name','table_type','seat_count')
        widgets = {
            'table_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'seat_count': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['table_type'].widget.attrs.update({'class':'form-control'})
