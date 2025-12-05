from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token

@admin.register(PerfilCliente)
class PerfilAdmin (admin.ModelAdmin):
    list_display = ["user"]
    search_fields = ['user']


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ["modelo","placa","ano","status"]
    search_fields = ["modelo","placa","ano","status"]
    list_filter = ["modelo","status"]


admin.site.register(Token)

