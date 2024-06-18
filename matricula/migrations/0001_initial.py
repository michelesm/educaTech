# Generated by Django 5.0.6 on 2024-06-18 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluno', '0001_initial'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateField()),
                ('ano_letivo', models.IntegerField()),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('pendente', 'Pendente'), ('cancelado', 'Cancelado'), ('transferido', 'Transferido')], max_length=20)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.turma')),
            ],
        ),
    ]
