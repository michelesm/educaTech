from django import forms
from .models import Professor


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'cpf', 'rg', 'endereco', 'telefone_contato', 'email', 'data_admissao']


