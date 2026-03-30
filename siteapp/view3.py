from django.shortcuts import render, redirect

EVENTS = []


def events(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        data = request.POST.get("data")
        evento = {"id": len(EVENTS) + 1, "nome": nome, "data": data}
        EVENTS.append(evento)

        return redirect("events")
    return render(request, "siteapp/events.html", {"events": EVENTS})


def view_event(request, event_id):
    evento = next((e for e in EVENTS if e["id"] == event_id), None)

    return render(request, "siteapp/view.html", {"evento": evento})
