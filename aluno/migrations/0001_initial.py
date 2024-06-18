# Generated by Django 5.0.6 on 2024-06-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('nome_pai', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_mae', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('rg', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone_contato', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('nome_responsavel', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='alunos/')),
            ],
        ),
    ]
