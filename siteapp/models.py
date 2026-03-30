from django.db import models


class Parent(models.Model):
    nome_pai = models.CharField(max_length=120)
    nome_filho = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.nome_pai} ({self.nome_filho})"


class EventAttendance(models.Model):
    # O id desta tabela representa o id do evento.
    id = models.PositiveIntegerField(primary_key=True)
    nome_evento = models.CharField(max_length=150)
    data_evento = models.DateField()
    # Lista com os ids dos pais presentes nesse evento.
    presencas = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Evento {self.id} - {self.nome_evento}"
