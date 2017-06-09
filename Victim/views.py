from django.views import generic
from .models import Victim


class IndexView(generic.ListView):
    template_name = 'Victim/index.html'
    context_object_name = 'Victims'

    def get_queryset(self):
        return Victim.objects.all()


class DetailView(generic.DetailView):
    model = Victim
    template_name = 'Victim/detail.html'
