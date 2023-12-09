from django.shortcuts import render
from django.views.generic import ListView

from .models import Thing


def home(request):
    return render(request, "favorites/home.html")


class ThingListView(ListView):
    model = Thing
