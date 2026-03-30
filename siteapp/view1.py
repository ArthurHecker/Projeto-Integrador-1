from django.shortcuts import redirect, render


def login_view(request):
    return render(request, "siteapp/login.html")


def logout_view(request):
    # Sem tela de logout: apenas redireciona para a home. Ela não tem html de visualização
    return redirect("home")


def register(request):
    return render(request, "siteapp/register.html")
