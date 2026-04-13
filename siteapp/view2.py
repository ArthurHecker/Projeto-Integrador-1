from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import EventAttendance, Parent


@login_required
def parents(request):
    status = ""
    error = ""

    if request.method == "POST":
        action = (request.POST.get("action") or "create").strip().lower()
        parent_id_raw = (request.POST.get("parent_id") or "").strip()
        nome_pai = (request.POST.get("parent_name") or "").strip()
        nome_filho = (request.POST.get("child_name") or "").strip()

        if action == "create":
            if not nome_pai or not nome_filho:
                error = "Preencha nome do pai e nome do filho para cadastrar."
            else:
                Parent.objects.create(nome_pai=nome_pai, nome_filho=nome_filho)
                status = "Pai cadastrado com sucesso."
        elif action == "update":
            if not parent_id_raw.isdigit():
                error = "Nao foi possivel identificar o pai para edicao."
            elif not nome_pai or not nome_filho:
                error = "Preencha nome do pai e nome do filho para atualizar."
            else:
                parent = Parent.objects.filter(id=int(parent_id_raw)).first()
                if parent is None:
                    error = "Registro de pai nao encontrado."
                else:
                    parent.nome_pai = nome_pai
                    parent.nome_filho = nome_filho
                    parent.save(update_fields=["nome_pai", "nome_filho"])
                    status = "Cadastro de pai atualizado com sucesso."
        elif action == "delete":
            if not parent_id_raw.isdigit():
                error = "Nao foi possivel identificar o pai para exclusao."
            else:
                deleted_count, _ = Parent.objects.filter(id=int(parent_id_raw)).delete()
                if deleted_count:
                    status = "Pai removido com sucesso."
                else:
                    error = "Registro de pai nao encontrado."
        else:
            error = "Acao invalida para a rota de pais."

    edit_parent = None
    edit_id = (request.GET.get("edit") or "").strip()
    if edit_id.isdigit():
        edit_parent = Parent.objects.filter(id=int(edit_id)).first()

    parents_list = Parent.objects.order_by("nome_pai", "nome_filho")
    return render(
        request,
        "siteapp/parents.html",
        {
            "parents_list": parents_list,
            "edit_parent": edit_parent,
            "status": status,
            "error": error,
        },
    )


@login_required
def attendances(request):
    status = ""
    error = ""

    eventos = EventAttendance.objects.order_by("-data_evento", "-id")
    parents_list = Parent.objects.order_by("nome_pai", "nome_filho")

    event_id_raw = ""
    if request.method == "POST":
        event_id_raw = (request.POST.get("event_id") or "").strip()
    else:
        event_id_raw = (request.GET.get("event_id") or "").strip()

    evento_selecionado = None
    if event_id_raw:
        if event_id_raw.isdigit():
            evento_selecionado = EventAttendance.objects.filter(id=int(event_id_raw)).first()
            if evento_selecionado is None:
                error = "Evento nao encontrado."
        else:
            error = "Evento invalido."

    if request.method == "POST":
        if evento_selecionado is None:
            error = "Selecione um evento valido para salvar as presencas."
        else:
            present_ids = [int(pid) for pid in request.POST.getlist("presentes") if pid.isdigit()]
            valid_present_ids = sorted(
                Parent.objects.filter(id__in=present_ids).values_list("id", flat=True)
            )
            evento_selecionado.presencas = valid_present_ids
            evento_selecionado.save(update_fields=["presencas"])
            status = "Presencas salvas com sucesso."

    presentes_ids = []
    if evento_selecionado is not None:
        presentes_ids = [int(pid) for pid in (evento_selecionado.presencas or []) if str(pid).isdigit()]

    return render(
        request,
        "siteapp/attendances.html",
        {
            "eventos": eventos,
            "evento_selecionado": evento_selecionado,
            "parents_list": parents_list,
            "presentes_ids": presentes_ids,
            "status": status,
            "error": error,
        },
    )
