from django.shortcuts import get_object_or_404, render, redirect
from .models import Receitas
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):

    receitas = Receitas.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }

    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)


def buscar(request):

    receitas = Receitas.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            receitas = receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': receitas
    }

    return render(request, 'receitas/buscar.html', dados)


def cria_receita(request):

    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_de_preparo = request.POST['modo_preparo']
        tempo_de_preparo = request.POST['tempo_preparo']
        rendimentos = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        # if campo_vazio(nome_receita):
        #     messages.error(request, 'O campo nome não pode ficar em branco')
        #     return redirect('cria_receita')
        # if campo_vazio(ingredientes):
        #     messages.error(request, 'O campo nome não pode ficar em branco')
        #     return redirect('cria_receita')
        # if campo_vazio(modo_de_preparo):
        #     messages.error(request, 'O campo nome não pode ficar em branco')
        #     return redirect('cria_receita')
        # if campo_vazio(tempo_de_preparo):
        #     messages.error(request, 'O campo nome não pode ficar em branco')
        #     return redirect('cria_receita')
        # if campo_vazio(rendimentos):
        #     messages.error(request, 'O campo nome não pode ficar em branco')
        #     return redirect('cria_receita')
        # if campo_vazio(categoria):
        #     messages.error(request, 'O campo nome não pode ficar em branco')
        #     return redirect('cria_receita')
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receitas.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_de_preparo=modo_de_preparo,tempo_de_preparo=tempo_de_preparo, rendimentos=rendimentos,categoria=categoria, foto_receita=foto_receita)
        receita.save()
        messages.success(request, 'Receita cadastrada com sucesso!')
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita_a_editar = {'receita': receita}
    return render(request, 'receitas/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        receita = Receitas.objects.get(pk=receita_id)
        receita.nome_receita = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_de_preparo = request.POST['modo_de_preparo']
        receita.tempo_de_preparo = request.POST['tempo_de_preparo']
        receita.redimentos = request.POST['rendimentos']
        receita.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            receita.foto_receita = request.FILES['foto_receita']
        receita.save()
        return redirect('dashboard')


def deleta_receita(request, receita_id):

    receita = get_object_or_404(Receitas, pk=receita_id)
    receita.delete()
    return redirect('dashboard')
