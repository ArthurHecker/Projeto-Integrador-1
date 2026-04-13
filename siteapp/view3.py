from django.shortcuts import render, redirect

EVENTS = []


def events(request):
    error_nome = None
    error_data = None

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        data = request.POST.get("data", "").strip()

        if not nome:
            error_nome = "Ops, você precisa inserir o nome do evento"

        if not data:
            error_data = "Ops, você precisa inserir uma data válida"

        if not error_nome and not error_data:
            EVENTS.append({
                "id": len(EVENTS) + 1,
                "nome": nome,
                "data": data
            })
            return redirect("events")

    return render(request, "siteapp/events.html", {
        "events": EVENTS,
        "error_nome": error_nome,
        "error_data": error_data
    })


def view_event(request, event_id):
    evento = next((e for e in EVENTS if e["id"] == int(event_id)), None)
    return render(request, "siteapp/view.html", {"evento": evento})


def edit_event(request, event_id):
    event_id = int(event_id)

    evento = next((e for e in EVENTS if e["id"] == event_id), None)

    if evento is None:
        return redirect("events")

    error_nome = None
    error_data = None

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        data = request.POST.get("data", "").strip()

        if not nome:
            error_nome = "Ops, você precisa inserir o nome do evento"

        if not data:
            error_data = "Ops, você precisa inserir uma data válida"

        if not error_nome and not error_data:
            evento["nome"] = nome
            evento["data"] = data
            return redirect("events")

    return render(request, "siteapp/edit_event.html", {
        "evento": evento,
        "error_nome": error_nome,
        "error_data": error_data
    })


def delete_event(_, event_id):
    event_id = int(event_id)
    global EVENTS

    EVENTS = [e for e in EVENTS if e["id"] != event_id]
    return redirect("events")