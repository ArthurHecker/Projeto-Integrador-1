import subprocess
import threading
import time
from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.utils import autoreload

from .view1 import login_view, logout_view, register
from .view2 import attendances, parents
from .view3 import events, view_event, edit_event, delete_event
from .models import EventAttendance


SERVER_INSTANCE_ID = str(time.time_ns())


@login_required
def home(request):
    events_db = EventAttendance.objects.order_by("-data_evento", "-id")[:6]
    home_events = [
        {"id": evento.id, "nome": evento.nome_evento, "data": evento.data_evento}
        for evento in events_db
    ]
    return render(request, "siteapp/home.html", {"events": home_events})


@login_required
def upload(request):
    if not settings.DEBUG:
        return HttpResponseForbidden("Rota disponivel apenas no ambiente de desenvolvimento.")

    allowed_branches = {"firmo", "fabio", "emmanuel", "arthur"}
    contexto = {
        "branches": ["firmo", "fabio", "emmanuel", "arthur"],
        "selected_branch": "",
        "status": "",
        "logs": [],
        "restart_pending": False,
        "server_instance_id": SERVER_INSTANCE_ID,
    }

    if request.method == "POST":
        selected_branch = (request.POST.get("branch") or "").strip().lower()
        contexto["selected_branch"] = selected_branch

        if selected_branch not in allowed_branches:
            contexto["status"] = "Branch invalida. Escolha uma das opcoes listadas."
            return render(request, "siteapp/upload.html", contexto)

        repo_dir = Path(__file__).resolve().parent.parent
        commands = [
            ["git", "fetch", "--all"],
            ["git", "pull"],
            ["git", "merge", "--no-edit", selected_branch],
        ]

        success = True
        logs = []

        for cmd in commands:
            completed = subprocess.run(
                cmd,
                cwd=repo_dir,
                text=True,
                capture_output=True,
                check=False,
            )
            logs.append(
                {
                    "command": " ".join(cmd),
                    "returncode": completed.returncode,
                    "stdout": completed.stdout.strip(),
                    "stderr": completed.stderr.strip(),
                }
            )   

            if completed.returncode != 0:
                success = False
                break

        contexto["logs"] = logs

        if success:
            contexto["status"] = (
                f"Mescla com '{selected_branch}' concluida. Reiniciando servidor de desenvolvimento..."
            )
            contexto["restart_pending"] = True

            def delayed_reload():
                time.sleep(1)
                # Solicita ao autoreloader do Django reiniciar o servidor em modo desenvolvimento.
                autoreload.trigger_reload(str(Path(__file__)))

            threading.Thread(target=delayed_reload, daemon=True).start()
        else:
            contexto["status"] = "Falha durante fetch/pull/merge. Veja os logs abaixo."

    return render(request, "siteapp/upload.html", contexto)


@login_required
def upload_health(request):
    if not settings.DEBUG:
        return HttpResponseForbidden("Rota disponivel apenas no ambiente de desenvolvimento.")
    return JsonResponse({"ok": True, "instance_id": SERVER_INSTANCE_ID})
