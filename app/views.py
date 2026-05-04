from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Iten, Usuario

from datetime import datetime

def home(request):
    if request.method == "GET":
        itens = Iten.objects.filter(active=True)
        return render(request, 'index.html', {'itens': itens})
    
    elif request.method == "POST":
        name_typing = request.POST.get('nome')
        phone_typing = request.POST.get('telefone')  
        seleted_products = request.POST.get('pedidos').split(",")  # get id list of selected products
        
        if name_typing and phone_typing:  # check if fields are filled in
            try:
                # create new user
                user = Usuario.objects.create(
                    user_name=name_typing,
                    phone=phone_typing,
                    current_date=datetime.now(),
                )
                # associate selected products to new user
                for pedido_id in seleted_products:
                    pedido = Iten.objects.get(pk=pedido_id)
                    user.ordered_items.add(pedido)

                  
                # redirect to confirmation page
                return render(request, 'confirmado.html')
            except Exception as e:
                # return error message
                return HttpResponse(f"Erro ao criar usuário: {str(e)}")
        else:
            # return error message if fields are not filled in
            return HttpResponse("Campos 'nome' e 'telefone' são obrigatórios!")

