from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Iten(models.Model):
    nome = models.CharField(max_length=40)
    ativo = models.BooleanField(default=True)
    quantidade = models.IntegerField(null=True, blank=True)  # Permitindo que seja opcional
    
    def __str__(self):
        return self.nome




class Usuario(models.Model):
    user_nome = models.CharField(max_length=60)
    telefone = PhoneNumberField(default=0)  # Adicionando um valor padrão temporário vazio
    data_pedida = models.DateTimeField()  # Define automaticamente a data de pedido
    itens_pedidos = models.ManyToManyField(Iten, related_name='usuarios')  # Relação muitos-para-muitos com Inten
    
    def __str__(self):
        return self.user_nome
