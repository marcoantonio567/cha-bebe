from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Iten, Usuario

from datetime import datetime

def home(request):
    if request.method == "GET":
        itens = Iten.objects.filter(ativo=True)
        return render(request, 'ver_itens.html', {'itens': itens})
    
    elif request.method == "POST":
        nome_digitado = request.POST.get('nome')
        telefone_digitado = request.POST.get('telefone')  
        pedidos_selecionados = request.POST.get('pedidos').split(",")  # Obter uma lista de IDs dos itens selecionados
        
        if nome_digitado and telefone_digitado:  # Verifica se os campos foram preenchidos
            try:
                # Cria o usuário
                usuario = Usuario.objects.create(
                    user_nome=nome_digitado,
                    telefone=telefone_digitado,
                    data_pedida=datetime.now(),
                )
                # Associa os pedidos selecionados ao novo usuário
                for pedido_id in pedidos_selecionados:
                    pedido = Iten.objects.get(pk=pedido_id)
                    usuario.itens_pedidos.add(pedido)

                  
                    
                return render(request, 'confirmado.html')
            except Exception as e:
                return HttpResponse(f"Erro ao criar usuário: {str(e)}")
        else:
            return HttpResponse("Campos 'nome' e 'email' são obrigatórios!")

