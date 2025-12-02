from rest_framework import viewsets 
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']

class PerfilClienteViewSet(viewsets.ModelViewSet):
    queryset = PerfilCliente.objects.all()
    serializer_class = PerfilClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'cnh', 'telefone', 'endereco']

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['modelo', 'placa', 'ano', 'status']

class AluguelViewSet(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['perfil_cliente_id', 'carro_id', 'funcionario_id', 'data_inicio', 'data_fim', 'valor']
