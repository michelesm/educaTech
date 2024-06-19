from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_completo', 'cpf', 'email', 'data_nascimento', 'nome_pai', 'nome_mae', 'rg', 'endereco',
                  'telefone_contato', 'nome_responsavel']


