from agendai.models import Escritorio, Cadeira, Sala_Reuniao, Agendamento_Escritorio, Agendamento_Reuniao
from rest_framework import  serializers

class escritorioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Escritorio
        fields = '__all__'

class cadeiraSerializer(serializers.ModelSerializer):
    escritorio = serializers.CharField()
    class Meta:
        model = Cadeira
        fields = ['id', 'numero_cadeira', 'escritorio', 'status_cadeira']



class sala_reuniaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala_Reuniao
        fields = '__all__'

class agendamento_escritorioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento_Escritorio
        fields = '__all__'

class agendamento_reuniaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento_Reuniao
        fields = '__all__'