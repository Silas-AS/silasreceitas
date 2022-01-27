from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def receita(requst):
    return render(requst, 'receita.html')