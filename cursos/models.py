from django.db import models


class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_curso


class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turma_nome = models.CharField(max_length=100)
    turma_ano = models.IntegerField()
    professor_responsavel = models.ForeignKey('professor.Professor', on_delete=models.CASCADE)
    horario_aulas = models.CharField(max_length=100)

    def __str__(self):
        return self.turma_nome
