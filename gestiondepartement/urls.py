from django.urls import path

from . import views

app_name = "gestiondepartement"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contribuer', views.contribuer, name = 'contribuer'),
    path('apropos', views.apropos, name = 'apropos'),
    path('missions', views.missions, name = 'missions'),
    path('faits', views.faits, name = 'faits'),

]