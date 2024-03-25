from django.shortcuts import render
from django.http import HttpResponse
from .models import Inten, Usuario

from datetime import datetime

def home(request):
    if request.method == "GET":
        itens = Inten.objects.filter(ativo=True)
        return render(request, 'ver_itens.html', {'itens': itens})
    
    elif request.method == "POST":
        nome_digitado = request.POST.get('nome')
        email_digitado = request.POST.get('email')  
        pedidos_selecionados = request.POST.getlist('presentes')  # Obter uma lista de IDs dos itens selecionados
        
        if nome_digitado and email_digitado:  # Verifica se os campos foram preenchidos
            try:
                # Cria o usuário
                usuario = Usuario.objects.create(
                    user_nome=nome_digitado,
                    email=email_digitado,
                    data_pedida=datetime.now(),
                )
                # Associa os pedidos selecionados ao novo usuário
                for pedido_id in pedidos_selecionados:
                    pedido = Inten.objects.get(pk=pedido_id)
                    usuario.itens_pedidos.add(pedido)
                    
                return HttpResponse("Usuário criado com sucesso!")
            except Exception as e:
                return HttpResponse(f"Erro ao criar usuário: {str(e)}")
        else:
            return HttpResponse("Campos 'nome' e 'email' são obrigatórios!")
