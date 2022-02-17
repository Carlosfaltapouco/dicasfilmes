from django.shortcuts import render
from .models import Dica


def index(request):
    dicas = Dica.objects.all()


    

    dados = {
        'dicas' : dicas
    }

    return render(request, 'index.html', dados)


def dica(request):
    return render(request, 'dica.html')
