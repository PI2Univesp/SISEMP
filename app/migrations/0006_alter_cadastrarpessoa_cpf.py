# Generated by Django 4.0.4 on 2022-06-25 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_cadastraratendimento_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarpessoa',
            name='cpf',
            field=models.BigIntegerField(),
        ),
    ]
