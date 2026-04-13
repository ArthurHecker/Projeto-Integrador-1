from django.shortcuts import render

from .view1 import login_view, logout_view, register
from .view2 import attendances, parents
from .view3 import events, view_event, edit_event, delete_event


def home(request):
    return render(request, "siteapp/home.html")
