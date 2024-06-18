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
    #horario_aulas = models.CharField(max_length=100)
    dia_da_semana = models.CharField(max_length=3, choices=DIAS_DA_SEMANA)
    horario = models.TimeField()

    def __str__(self):
        return self.turma_nome







def __str__(self):
    return f'{self.get_dia_da_semana_display()} às {self.horario}'


class Meta:
    verbose_name = 'Horário de Aula'
    verbose_name_plural = 'Horários de Aulas'
