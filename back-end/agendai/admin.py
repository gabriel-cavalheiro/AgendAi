from django.contrib import admin
from agendai.models import Consultor, Escritorio, Sala_Reuniao, Agendamento_Escritorio, Agendamento_Reuniao


@admin.register(Consultor)
class ConsultorAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'nome_consultor', 'email_consultor']
    list_per_page = 3

@admin.register(Escritorio)
class EscritorioAdmin(admin.ModelAdmin):
    list_display = ['local_escritorio', 'percentual_legislacao', 'capacidade_total']
    list_per_page = 3

@admin.register(Sala_Reuniao)
class EscritorioAdmin(admin.ModelAdmin):
    list_display = ['numero_sala', 'escritorio_reuniao']
    list_per_page = 3

@admin.register(Agendamento_Escritorio)
class Agendamento_EscritorioAdmin(admin.ModelAdmin):
    list_display = ['lugar_escritorio', 'data_inicio', 'data_fim', 'cadeira', 'consultor_escritorio', 'status_escritorio']
    list_per_page = 3

@admin.register(Agendamento_Reuniao)
class Agendamento_ReuniaoAdmin(admin.ModelAdmin):
    list_display = ['lugar_reuniao', 'data_hora_inicio', 'data_hora_fim', 'sala_reuniao', 'consultor_reuniao']
    list_per_page = 3
