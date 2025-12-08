from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PerfilClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilCliente
        fields = '__all__'

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class AluguelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluguel
        fields = '__all__'