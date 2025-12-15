from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from .models import *
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login


class UserViewSet(viewsets.ModelViewSet): # Lembret - Adm e funcionario criar cliente
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']
    permission_classes = [IsFuncionario]  


class   PerfilClienteViewSet(viewsets.ModelViewSet): # lembret - Funcionario CRUD, Cliente ver
    queryset = PerfilCliente.objects.all()
    serializer_class = PerfilClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'cnh', 'telefone']
    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            return [IsAuthenticated()]
        return [IsFuncionario()]

    @action(detail=True, methods=['get'], permission_classes=[IsFuncionario])
    def alugueis(self, request, pk=None):
        perfil = self.get_object()
        alugueis = perfil.alugueis.all()
        page = self.paginate_queryset(alugueis)
        if page is not None:
            serializer = AluguelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AluguelSerializer(alugueis, many=True)
        return Response(serializer.data)


class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['modelo', 'placa', 'ano', 'status']
    permission_classes = [IsFuncionarioOrReadOnly]


class AluguelViewSet(viewsets.ModelViewSet): # lemnbrete - 
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['perfil_cliente', 'carro', 'funcionario', 'data_inicio', 'data_fim']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [IsFuncionario()]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated]) # Lembrete - usuario ver no perfil os alugueis
    def me_alugueis(self, request):
        try:
            perfil = request.user.perfil
        except PerfilCliente.DoesNotExist:
            return Response([], status=status.HTTP_200_OK)
        alugueis = Aluguel.objects.filter(perfil_cliente=perfil)
        page = self.paginate_queryset(alugueis)
        if page is not None:
            serializer = AluguelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AluguelSerializer(alugueis, many=True)
        return Response(serializer.data)

    def perform_destroy(self, instance): #liberar carro
        instance.delete()

    def perform_create(self, serializer):
        funcionario = serializer.validated_data.get('funcionario', None)
        if funcionario is None:
            serializer.save(funcionario=self.request.user)
        else:
            serializer.save()



def is_funcionario(user):
    if not user or not user.is_authenticated:
        return False
    if user.is_staff:
        return True
    return user.groups.filter(name__iexact='Funcionarios').exists()

@login_required
def historico_cliente(request):
    
    try:
        perfil = request.user.perfil  
    except PerfilCliente.DoesNotExist:
        return render(request, 'historico_cliente.html', {
            'error': 'Você não possui um perfil de cliente.',
            'alugueis': [],
            'cliente': None
        })

    alugueis = Aluguel.objects.filter(perfil_cliente=perfil).select_related('carro', 'funcionario').order_by('-data_inicio')
    return render(request, 'historico_cliente.html', {
        'alugueis': alugueis,
        'cliente': perfil,
        'is_funcionario_view': False,
    })

@login_required
@user_passes_test(is_funcionario)
def historico_perfil(request, pk):
    perfil = get_object_or_404(PerfilCliente, pk=pk)
    alugueis = Aluguel.objects.filter(perfil_cliente=perfil).select_related('carro', 'funcionario').order_by('-data_inicio')
    return render(request, 'concessionaria/historico_cliente.html', {
        'alugueis': alugueis,
        'cliente': perfil,
        'is_funcionario_view': True,
    })

def login_cliente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # cria sessão usuario
            if user.is_staff or user.is_superuser:
                return redirect('/admin/')

            
            return redirect('historico-me')  # redireciona para o histórico do cliente
        
        
        else:
            return render(request, 'login.html', {"error": True})

    return render(request, 'login.html')



