from django import forms
from.models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ('aluno', 'tipo', 'data_emissao', 'conteudo')