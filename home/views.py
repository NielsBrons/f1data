from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Races, Events, Circuit


class RacesListView(ListView):
    model = Races

class RacesDetailView(DetailView):
    model = Races

class eventsDetailView(DetailView):
    model = Events

class CircuitDetailView(DetailView):
    model = Circuit