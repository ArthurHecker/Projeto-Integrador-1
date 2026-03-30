from django.shortcuts import render
from datetime import date

from .models import EventAttendance


def parents(request):
    return render(request, "siteapp/parents.html")


def attendances(request):
    return render(request, "siteapp/attendances.html")
