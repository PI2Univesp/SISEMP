from django.contrib import admin

from .models import CadastrarAtendimento, CadastrarPessoa

# Register your models here.
admin.site.register(CadastrarAtendimento)
admin.site.register(CadastrarPessoa)