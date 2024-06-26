from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = (
        'nome_completo', 'data_nascimento', 'nome_pai', 'nome_mae', 'cpf', 'rg', 'endereco', 'telefone_contato',
        'email', 'nome_responsavel')

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if cpf and not cpf.isdigit():
            raise forms.ValidationError('O CPF deve conter apenas dígitos.')
        if cpf and Aluno.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Já existe um aluno cadastrado com esse CPF.')
        return cpf

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and Aluno.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um aluno cadastrado com esse e-mail.')
        return email
