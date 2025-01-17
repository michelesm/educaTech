# Generated by Django 5.0.6 on 2024-06-18 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='horario_aulas',
        ),
        migrations.AddField(
            model_name='turma',
            name='dia_da_semana',
            field=models.CharField(choices=[('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'), ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira'), ('SAB', 'Sábado'), ('DOM', 'Domingo')], default=None, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='horario',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]
