from django.conf.urls import url
from . import views

urlpatterns = [
    # /victim/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /victim/<victim_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]