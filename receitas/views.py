from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Receitas

def index(request):

    receitas = Receitas.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)


def buscar(request):
    return render(request, 'buscar.html')