from django.db import models
from aluno.models import Aluno  # Certifique-se de substituir 'aluno' pelo nome correto do app

class Documento(models.Model):
    TIPOS_DOCUMENTO = [
        ('declaracao', 'Declaração de Matrícula'),
        ('comparecimento', 'Declaração de Comparecimento'),
        ('certificado', 'Certificado de Conclusão'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    data_emissao = models.DateField()
    conteudo = models.TextField()

    def __str__(self):
        return f"{self.tipo} - {self.aluno.nome_completo}"


# Create your models here.
