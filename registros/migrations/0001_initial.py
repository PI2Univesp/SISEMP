# Generated by Django 4.0.4 on 2022-05-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=999, verbose_name='Serviço')),
            ],
        ),
        migrations.CreateModel(
            name='CadastroPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('cpf', models.DecimalField(decimal_places=1, max_digits=13)),
                ('data_nacimento', models.DecimalField(decimal_places=1, max_digits=8)),
                ('telefone', models.DecimalField(decimal_places=1, max_digits=14)),
                ('email', models.CharField(max_length=70)),
                ('atendente', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=999, verbose_name='Serviço')),
            ],
        ),
    ]