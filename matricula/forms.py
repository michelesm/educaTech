from django import forms
from .models import Matricula, Turma
from cursos.models import Curso

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'data_matricula', 'ano_letivo', 'curso', 'turma', 'status']

    turma = forms.ModelChoiceField(queryset=Turma.objects.all(), empty_label="Selecione uma turma")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['turma'].queryset = Turma.objects.none()
        model = Matricula

        if 'curso' in self.data:
            try:
                curso_id = int(self.data.get('curso'))
                self.fields['turma'].queryset = Turma.objects.filter(curso_id=curso_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['turma'].queryset = self.instance.curso.turma_set.all()