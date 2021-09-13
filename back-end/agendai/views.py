from agendai.models import Escritorio
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.contrib import messages



def lista_local_escritorio(request):
    escritorios = Escritorio.objects.all()
    dados =  {'escritorio': escritorios}
    return render(request, 'localidade.html', dados)

def escolha(request):
    pass
    return render(request, 'escolha.html')

def agendamento_reuniao(request):
    pass