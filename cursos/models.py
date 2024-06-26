from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_curso


class Turma(models.Model):
    DIAS_DA_SEMANA = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turma_nome = models.CharField(max_length=100)
    turma_ano = models.IntegerField()
    professor_responsavel = models.ForeignKey('professor.Professor', on_delete=models.CASCADE)
    dia_da_semana = models.CharField(max_length=3, choices=DIAS_DA_SEMANA)
    horario = models.TimeField()
    data_inicio = models.DateField()
    quantidade_aulas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])

    def __str__(self):
        return self.turma_nome

    def get_horario_display(self):
        return f'{self.get_dia_da_semana_display()} às {self.horario}'

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'