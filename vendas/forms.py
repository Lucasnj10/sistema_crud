from django import forms
from .models import Cliente, Venda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type':'date'})
        }

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'produto', 'quantidade', 'data_venda']
        widgets = {
            'data_venda': forms.DateInput(attrs={'type': 'date'}),
        }
