from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token

@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'cnh', 'telefone')

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'placa', 'ano', 'status')
    list_filter = ('status', 'ano')

@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('id', 'perfil_cliente', 'carro', 'funcionario', 'data_inicio', 'data_fim', 'valor')
    list_filter = ('funcionario', 'data_inicio')
