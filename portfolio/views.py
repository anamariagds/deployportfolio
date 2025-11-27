from django.shortcuts import render, redirect
#from .dados import habilidades, projetos
from .models import Habilidade, Projeto
#from .forms import ContatoForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    habilidades = Habilidade.objects.all()
    return render(request, 'home.html', {'habilidades': habilidades})
def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

def detalhes_projeto(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    return render(request, 'detalhes_projeto.html', {'projeto': projeto})

# def lista_projetos(request):
#     return render(request, 'projetos.html', {'projetos': projetos})

# def detalhes_projeto(request, id_projeto):
#     projeto = projetos.get(id_projeto)
#     return render(request, 'detalhes_projeto.html', {'projeto': projeto})