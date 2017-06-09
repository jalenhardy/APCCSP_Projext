from django.conf.urls import url
from . import views

urlpatterns = [
    # /activist/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /activist/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]