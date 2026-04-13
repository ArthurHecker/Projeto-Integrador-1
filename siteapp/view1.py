from django.shortcuts import redirect, render
from .models import Pai


def login_view(request):
    return render(request, "siteapp/login.html")


def logout_view(request):
    # Sem tela de logout: apenas redireciona para a home. Ela não tem html de visualização
    return redirect("home")


def register(request):
    return render(request, "siteapp/register.html")
#adicionando a lista de pais para que seja possivel a vizualização
def parents_list(request):
    pais = Pai.objects.all()
    return render(request, "siteapp/parents_list.html", {"pais": pais})
