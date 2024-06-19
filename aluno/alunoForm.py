from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('nome_completo', 'cpf', 'email',)
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
