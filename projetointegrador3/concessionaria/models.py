from django.db import models
from django.contrib.auth.models import User,Group



class PerfilCliente(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnh = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=13)
    endereco = models.TextField()

    def __str__(self):
        return self.user.username

class Carro(models.Model):
    carro_status = [
        ('Livre','Livre'),
        ('Alugado','Alugado'),
        ('Manutenção','Manutenção')
    ]


    id_carro = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length= 50)
    placa = models.CharField(max_length=7, unique=True)
    ano = models.CharField(4)
    status = models.CharField(choices=carro_status, default='Livre')

    def __str__(self):
        return self.id_carro

class Aluguel(models.Model):
    id_aluguel = models.AutoField(primary_key=True)
    perfil_cliente_id = models.ForeignKey(PerfilCliente, on_delete= models.CASCADE)
    carro_id = models.ForeignKey(Carro, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, related_name=("Alugueis_registrados"))
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"{self.id_aluguel} - {self.perfil_cliente_id.user.username}"
    








