from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def lista(request):
    pesquisa = request.GET.get('pesquisa', '')
    if pesquisa == '':
        pessoas = Pessoa.objects.all()
    else: 
        pessoas = Pessoa.objects.filter(bio__contains=pesquisa)
    context = {'pessoas': pessoas}
    return render(request, 'core/lista.html', context)

def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    context = {'pessoa': pessoa}
    return render(request, 'core/detalhe.html', context)