from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import EventAttendance, Parent


def _serialize_event(evento):
    return {
        "id": evento.id,
        "nome": evento.nome_evento,
        "data": evento.data_evento,
    }


@login_required
def events(request):
    error_nome = None
    error_data = None

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        data_raw = request.POST.get("data", "").strip()
        data_evento = None

        if not nome:
            error_nome = "Ops, você precisa inserir o nome do evento"

        if not data_raw:
            error_data = "Ops, você precisa inserir uma data válida"
        else:
            try:
                data_evento = date.fromisoformat(data_raw)
            except ValueError:
                error_data = "Ops, você precisa inserir uma data válida"

        if not error_nome and not error_data:
            last_id = EventAttendance.objects.order_by("-id").values_list("id", flat=True).first() or 0
            EventAttendance.objects.create(
                id=last_id + 1,
                nome_evento=nome,
                data_evento=data_evento,
                presencas=[],
            )
            return redirect("events")

    events_db = EventAttendance.objects.order_by("-data_evento", "-id")
    events_list = [_serialize_event(evento) for evento in events_db]

    return render(request, "siteapp/events.html", {
        "events": events_list,
        "error_nome": error_nome,
        "error_data": error_data
    })


@login_required
def view_event(request, event_id):
    evento_db = EventAttendance.objects.filter(id=int(event_id)).first()

    if evento_db is None:
        return render(request, "siteapp/view.html", {"evento": None, "pais_presentes": []})

    parent_ids = [int(pid) for pid in (evento_db.presencas or []) if str(pid).isdigit()]
    pais_presentes = Parent.objects.filter(id__in=parent_ids).order_by("nome_pai", "nome_filho")
    evento = _serialize_event(evento_db)

    return render(
        request,
        "siteapp/view.html",
        {"evento": evento, "pais_presentes": pais_presentes},
    )


@login_required
def edit_event(request, event_id):
    evento_db = EventAttendance.objects.filter(id=int(event_id)).first()

    if evento_db is None:
        return redirect("events")

    error_nome = None
    error_data = None

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        data_raw = request.POST.get("data", "").strip()
        data_evento = None

        if not nome:
            error_nome = "Ops, você precisa inserir o nome do evento"

        if not data_raw:
            error_data = "Ops, você precisa inserir uma data válida"
        else:
            try:
                data_evento = date.fromisoformat(data_raw)
            except ValueError:
                error_data = "Ops, você precisa inserir uma data válida"

        if not error_nome and not error_data:
            evento_db.nome_evento = nome
            evento_db.data_evento = data_evento
            evento_db.save(update_fields=["nome_evento", "data_evento"])
            return redirect("events")

    evento = _serialize_event(evento_db)

    return render(request, "siteapp/edit_event.html", {
        "evento": evento,
        "error_nome": error_nome,
        "error_data": error_data
    })


@login_required
def delete_event(_, event_id):
    EventAttendance.objects.filter(id=int(event_id)).delete()
    return redirect("events")