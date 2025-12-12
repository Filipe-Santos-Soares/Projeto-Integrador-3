from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    cnh = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=13)
    endereco = models.TextField()

    def __str__(self):
        return f"{self.user.username} - CNH: {self.cnh}"


class Carro(models.Model):
    carro_status = [
        ('Livre', 'Livre'),
        ('Alugado', 'Alugado'),
        ('Manutenção', 'Manutenção'),
    ]

    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7, unique=True)
    ano = models.CharField(max_length=4)
    status = models.CharField(max_length=20, choices=carro_status, default='Livre')

    def __str__(self):
        return f"{self.modelo} ({self.placa}) - {self.status}"


class Aluguel(models.Model):
    perfil_cliente = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE, related_name="alugueis")
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name="alugueis")
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alugueis_registrados")
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # maior precisão

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Aluguel #{self.pk} - {self.carro.placa} por {self.perfil_cliente.user.username}"

    class Meta:
        ordering = ['-data_inicio']
