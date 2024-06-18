from django.db import models
from aluno.models import Aluno
from professor.models import Professor
from cursos.models import Turma, Curso  # Importar o novo modelo Turma do app cursos


class Matricula(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('pendente', 'Pendente'),
        ('cancelado', 'Cancelado'),
        ('transferido', 'Transferido')
    ]

    # Campos da Matrícula
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_matricula = models.DateField()
    ano_letivo = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)  # Referência à classe Turma no app cursos
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.aluno.nome_completo} - {self.turma.turma_nome} ({self.turma.curso.nome_curso}) - Status: {self.status}"
