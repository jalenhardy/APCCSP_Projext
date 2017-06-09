from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^activist/', include('activist.urls', namespace='activist')),
    url(r'^victims/', include('Victim.urls', namespace='victim')),

]