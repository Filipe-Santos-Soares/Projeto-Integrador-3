from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from datetime import date

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    groups = serializers.SlugRelatedField(slug_field='name', queryset=Group.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active', 'is_staff', 'groups']
        read_only_fields = ['is_staff']  

    def create(self, validated_data):
        groups = validated_data.pop('groups', [])
        password = validated_data.pop('password')
        user = User(**validated_data)
        try:
            validate_password(password, user)
        except ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})
        user.set_password(password)
        user.save()
        if groups:
            user.groups.set(groups)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        if password:
            instance.set_password(password)
        instance.save()
        if groups is not None:
            instance.groups.set(groups)
        return instance


class PerfilClienteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PerfilCliente
        fields = ['id', 'user', 'cnh', 'telefone', 'endereco']


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id', 'modelo', 'placa', 'ano', 'status']
        read_only_fields = ['status']  


class AluguelSerializer(serializers.ModelSerializer):
    perfil_cliente = serializers.PrimaryKeyRelatedField(queryset=PerfilCliente.objects.all())
    carro = serializers.PrimaryKeyRelatedField(queryset=Carro.objects.all())
    funcionario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Aluguel
        fields = ['id', 'perfil_cliente', 'carro', 'funcionario', 'data_inicio', 'data_fim', 'valor', 'criacao', 'atualizacao']
        read_only_fields = ['criacao', 'atualizacao']

    def validate(self, data):
        if data['data_inicio'] > data['data_fim']:
            raise serializers.ValidationError("data inicial maior que a final.")

        carro = data['carro']
        if carro.status == 'Alugado':
            if self.instance is None:
                raise serializers.ValidationError("Carro não está disponível.")
            else:
                if self.instance.carro != carro:
                    raise serializers.ValidationError("Carro não está disponível.")
        return data

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
