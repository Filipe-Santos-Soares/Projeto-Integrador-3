from django.db import models
from django.contrib.auth.models import User



class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user_id = models.ForeignKey(8888, on_delete = models.CASCADE)
    cnh = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    endereco = models.TextField()

    def __str__(self):
        return self.id_cliente

class Carro(models.Model):
    carro_status = [
        ('Livre','Livre'),
        ('Alugado','Alugado'),
        ('Manutenção','Manutenção')
    ]


    id_carro = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length= 50)
    placa = models.CharField(7)
    ano = models.CharField(4)
    status = models.CharField(choices=carro_status)

    def __str__(self):
        return self.id_carro

class Aluguel(models.Model):
    id_aluguel = models.AutoField(primary_key=True)
    perfil_cliente_id = models.ForeignKey(PerfilCliente, on_delete= models.CASCADE)
    carro_id = models.ForeignKey(Carro, on_delete=models.CASCADE)
    #funcionario_id = ()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.IntegerField()

    def __str__(self):
        return self.id_aluguel
    

class funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=150)






