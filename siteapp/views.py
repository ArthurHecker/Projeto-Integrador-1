from django.shortcuts import render


def home(request):
    return render(request, "siteapp/home.html")


def sobre(request):
    return render(request, "siteapp/sobre.html")


def servicos(request):
    return render(request, "siteapp/servicos.html")


def contato(request):
    return render(request, "siteapp/contato.html")
