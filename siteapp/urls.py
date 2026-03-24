from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("events/", views.events, name="events"),
    path('view/<int:event.id>', views.view_event, name='view_event'),
    path("servicos/", views.servicos, name="servicos"),
    path("contato/", views.contato, name="contato"),
]
