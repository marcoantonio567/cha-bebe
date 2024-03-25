from django.db import models
from datetime import datetime

class Inten(models.Model):
    nome = models.CharField(max_length=40)
    ativo = models.BooleanField(default=True)
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    user_nome = models.CharField(max_length=60)
    email = models.EmailField(unique=True)  # Garante e-mails únicos
    data_pedida = models.DateTimeField(auto_now_add=True)  # Define automaticamente a data de pedido
    itens_pedidos = models.ManyToManyField(Inten, related_name='usuarios')  # Relação muitos-para-muitos com Inten
    
    def __str__(self):
        return self.user_nome
