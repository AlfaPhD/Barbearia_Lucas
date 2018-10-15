from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from agenda.models import *
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['apelido', 'senha','nome','email','celular']

def indexCliente(request):
    cliente = Cliente.objects.all()
    context = {'clientes': cliente}
    return render(request, 'cliente/index.html',context)

def createCliente(request):
    cliente = Cliente()
    if request.method == 'POST':
        cliente.apelido = request.POST['apelido']
        cliente.senha = request.POST['senha']
        cliente.nome = request.POST['nome']
        cliente.email = request.POST['email']
        cliente.celular = request.POST['celular']
        cliente.save()
        return HttpResponseRedirect('/cliente')
    else:
        return render(request, 'cliente/create.html')
def editCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    context = {'clientes': cliente}
    return render(request, 'crud/edit.html', context)

def updateCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.LOGIN = request.POST['login']
    cliente.SENHA = request.POST['senha']
    cliente.NOME = request.POST['nome']
    cliente.EMAIL = request.POST['email']
    cliente.CELULAR = request.POST['celular']
    cliente.APELIDO = request.POST['apelido']
    cliente.save()
    return redirect('/cliente')


def deleteCliente(request, id):
    professor = Cliente.objects.get(id=id)
    professor.delete()
    return redirect('/cliente')