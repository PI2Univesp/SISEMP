# Generated by Django 4.0.4 on 2022-06-09 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cadastraratendimento_cadastrarpessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastraratendimento',
            name='cadastrarpessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cadastrarpessoa', verbose_name='CPF'),
        ),
    ]