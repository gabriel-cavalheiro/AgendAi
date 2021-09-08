from django.db import models

class Consultor(models.Model):
    matricula = models.CharField(max_length=5, unique=True, blank=False, null=False, verbose_name='Matricula')
    nome_consultor = models.CharField(max_length=150, blank=False, null=False,  verbose_name='Nome')
    email_consultor = models.EmailField(max_length=60, blank=False, null=False, verbose_name='E-mail')

    class Meta:
        db_table = 'consultor'

    def __str__(self):
        return self.nome_consultor

class Escritorio(models.Model):
    local_escritorio = models.CharField(max_length=150, blank=False, null=False, verbose_name='Local do Escritorio')
    percentual_legislacao = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True, verbose_name='Percentual da Legislação')
    capacidade_total = models.IntegerField(blank=False, null=True, verbose_name='Capacidade Total')

    class Meta:
        db_table = 'escritorio'

    def __str__(self):
        return self.local_escritorio


class Sala_Reuniao(models.Model):
    numero_sala = models.IntegerField(blank=False, null=False,unique=True, verbose_name='Número da Sala')
    escritorio_reuniao = models.ForeignKey(Escritorio, on_delete=models.DO_NOTHING, verbose_name='Escritorio de Reunião')

    class Meta:
        db_table = 'sala_reuniao'

    def __str__(self):
        return self.numero_sala

class Agendamento_Escritorio(models.Model):
    data_inicio = models.DateField(blank=False, null=False, verbose_name='Data Inicio')
    data_fim = models.DateField(blank=False, null=False, verbose_name='Data Fim')
    cadeira = models.IntegerField(blank=False, null=False, verbose_name='Lugar')
    status_escritorio = models.BooleanField(verbose_name='Status Agendamento Escritorio')
    lugar_escritorio = models.ForeignKey(Escritorio, on_delete=models.DO_NOTHING, verbose_name='Escritorio')
    consultor_escritorio = models.ForeignKey(Consultor, on_delete=models.DO_NOTHING, verbose_name='Consultor')

    class Meta:
        db_table = 'agendamento_escritorio'

    def __str__(self):
        return self.data_inicio

class Agendamento_Reuniao(models.Model):
    data_hora_inicio = models.DateTimeField(blank=False, null=False, verbose_name='Data e Hora do Inicio')
    data_hora_fim = models.DateTimeField(blank=False, null=False, verbose_name='Data e Hora do Fim')
    status_reuniao = models.BooleanField(verbose_name='Status Agendamento Reunião')
    lugar_reuniao = models.ForeignKey(Escritorio, on_delete=models.DO_NOTHING, verbose_name='Escritorio')
    consultor_reuniao = models.ForeignKey(Consultor, on_delete=models.DO_NOTHING, verbose_name='Consultor')
    sala_reuniao = models.ForeignKey(Sala_Reuniao, on_delete=models.DO_NOTHING, verbose_name='Numero da Sala de Reunião')

    class Meta:
        db_table = 'agendamento_reuniao'

    def __str__(self):
        return self.data_hora_inicio