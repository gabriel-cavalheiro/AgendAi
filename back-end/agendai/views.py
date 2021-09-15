from agendai.models import Escritorio, Cadeira, Sala_Reuniao, Agendamento_Escritorio, Agendamento_Reuniao
from rest_framework import viewsets
from agendai.serializers import escritorioSerializer, cadeiraSerializer, sala_reuniaoSerializer, agendamento_reuniaoSerializer, agendamento_escritorioSerializer

class escritorioViewSet(viewsets.ModelViewSet):
    queryset = Escritorio.objects.all()
    serializer_class = escritorioSerializer

class cadeiraViewSet(viewsets.ModelViewSet):
    queryset = Cadeira.objects.all()
    serializer_class = cadeiraSerializer

class sala_reuniaoViewSet(viewsets.ModelViewSet):
    queryset = Sala_Reuniao.objects.all()
    serializer_class = sala_reuniaoSerializer

class agendamento_escritorioViewSet(viewsets.ModelViewSet):
    queryset = Agendamento_Escritorio.objects.all()
    serializer_class = agendamento_escritorioSerializer

class agendamento_reuniaoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento_Reuniao.objects.all()
    serializer_class = agendamento_reuniaoSerializer