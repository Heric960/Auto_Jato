from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    if request.method == 'GET':
        return render(request, 'clientes.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carro = request.POST.getlist('carro')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')
        return HttpResponse('teste')    
