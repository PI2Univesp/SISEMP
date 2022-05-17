# Generated by Django 4.0.4 on 2022-05-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_alter_cadastropessoa_cpf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('cpf', models.DecimalField(decimal_places=0, max_digits=13)),
                ('dataNascimento', models.DecimalField(decimal_places=0, max_digits=8, verbose_name='Data de Nascimento')),
                ('telefone', models.DecimalField(decimal_places=0, max_digits=14)),
                ('email', models.CharField(max_length=70)),
                ('servico', models.CharField(max_length=225, verbose_name='Serviço')),
                ('atendente', models.CharField(max_length=999)),
            ],
        ),
        migrations.DeleteModel(
            name='Atendente',
        ),
        migrations.DeleteModel(
            name='CadastroPessoa',
        ),
        migrations.DeleteModel(
            name='Servico',
        ),
    ]
