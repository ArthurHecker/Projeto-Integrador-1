from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme


DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"


def _ensure_default_admin_user():
    """Garante que o usuario padrao exista com a credencial combinada."""
    user_model = get_user_model()
    user, created = user_model.objects.get_or_create(username=DEFAULT_USERNAME)
    if created or not user.check_password(DEFAULT_PASSWORD):
        user.set_password(DEFAULT_PASSWORD)
        user.is_staff = True
        user.save()


def _get_safe_next_url(request, candidate):
    if not candidate:
        return ""
    if url_has_allowed_host_and_scheme(candidate, allowed_hosts={request.get_host()}):
        return candidate
    return ""


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    error = ""
    success = ""
    next_url = request.POST.get("next") or request.GET.get("next") or ""
    safe_next_url = _get_safe_next_url(request, next_url)

    if request.GET.get("registered") == "1":
        success = "Cadastro concluido. Entre com admin/admin."

    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        password = request.POST.get("password") or ""

        if username != DEFAULT_USERNAME or password != DEFAULT_PASSWORD:
            error = "Credenciais invalidas. Use usuario admin e senha admin."
        else:
            _ensure_default_admin_user()
            user = authenticate(request, username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD)
            if user is None:
                error = "Falha ao autenticar o usuario admin. Tente novamente."
            else:
                login(request, user)
                return redirect(safe_next_url or "home")

    return render(
        request,
        "siteapp/login.html",
        {"error": error, "success": success, "next": safe_next_url},
    )


def logout_view(request):
    logout(request)
    return redirect("login")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    error = ""

    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        password1 = request.POST.get("password1") or ""
        password2 = request.POST.get("password2") or ""

        if not username or not password1 or not password2:
            error = "Preencha todos os campos."
        elif password1 != password2:
            error = "As senhas nao coincidem."
        elif username != DEFAULT_USERNAME or password1 != DEFAULT_PASSWORD:
            error = "Neste projeto, o acesso padrao e fixo: usuario admin e senha admin."
        else:
            _ensure_default_admin_user()
            return redirect("/login/?registered=1")

    return render(request, "siteapp/register.html", {"error": error})
