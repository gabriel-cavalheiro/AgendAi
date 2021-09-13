from django.contrib import admin
from django.urls import path, include
from agendai import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/local/')),
    path('local/', views.lista_local_escritorio),
    path('escolha/', views.escolha),
    path('agendamento_reuniao', views.agendamento_reuniao),

]
