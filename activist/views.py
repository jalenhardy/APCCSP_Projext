from django.views import generic
from .models import Activist


class IndexView(generic.ListView):
    template_name = 'activist/activist.html'
    context_object_name = 'Activists'

    def get_queryset(self):
        return Activist.objects.all()


class DetailView(generic.DetailView):
    model = Activist
    template_name = 'activist/details.html'
