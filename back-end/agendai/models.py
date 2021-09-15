from django.db import models

class Escritorio(models.Model):
    local_escritorio = models.CharField(max_length=150, blank=False, null=False, verbose_name='Local do Escritorio')
    percentual_legislacao = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True, verbose_name='Percentual da Legislação')
    capacidade_total = models.PositiveIntegerField(blank=False, null=True, verbose_name='Capacidade Total')

    class Meta:
        verbose_name_plural = 'Escritorios'
        db_table = 'escritorio'

    def __str__(self):
        return self.local_escritorio

class Cadeira(models.Model):
    numero_cadeira = models.PositiveIntegerField(blank=False, null=False, verbose_name='Numero Cadeira')
    local_escritorio_cadeira = models.ForeignKey(Escritorio, on_delete= models.DO_NOTHING, verbose_name='Local Cadeira')
    status_cadeira = models.BooleanField(default=True, verbose_name='Status Cadeira')

    class Meta:
        verbose_name_plural = 'Cadeiras'
        db_table = 'cadeira'

    def __str__(self):
        return f'{self.numero_cadeira}'

class Sala_Reuniao(models.Model):
    numero_sala = models.PositiveIntegerField(blank=False, null=False, verbose_name='Número da Sala')
    escritorio_reuniao = models.ForeignKey(Escritorio, on_delete=models.CASCADE, verbose_name='Escritorio de Reunião')

    class Meta:
        verbose_name_plural = 'Sala_Reuniões'
        db_table = 'sala_reuniao'

    def __str__(self):
        return f'{self.numero_sala}'


class Agendamento_Escritorio(models.Model):
    data_inicio = models.DateField(blank=False, null=False, verbose_name='Data Inicio')
    data_fim = models.DateField(blank=False, null=False, verbose_name='Data Fim')
    lugar_cadeira = models.ForeignKey(Cadeira, on_delete= models.DO_NOTHING, verbose_name='Cadeira')
    status_escritorio = models.BooleanField(default=True, verbose_name='Status Agendamento Escritorio')
    lugar_escritorio = models.ForeignKey(Escritorio, on_delete=models.DO_NOTHING, verbose_name='Escritorio')


    class Meta:
        verbose_name_plural = 'Agendamentos dos Escritorios'
        db_table = 'agendamento_escritorio'

    def __str__(self):
        return f'{self.data_inicio}'

class Agendamento_Reuniao(models.Model):
    data_hora_inicio = models.DateTimeField(blank=False, null=False, verbose_name='Data e Hora do Inicio')
    data_hora_fim = models.DateTimeField(blank=False, null=False, verbose_name='Data e Hora do Fim')
    status_reuniao = models.BooleanField(default=True, verbose_name='Status Agendamento Reunião')
    lugar_reuniao = models.ForeignKey(Escritorio, on_delete=models.DO_NOTHING, verbose_name='Escritorio')
    sala_reuniao = models.ForeignKey(Sala_Reuniao, on_delete=models.DO_NOTHING, verbose_name='Numero da Sala')

    class Meta:
        verbose_name_plural = 'Agendamentos das Reuniões'
        db_table = 'agendamento_reuniao'

    def __str__(self):
        return f'{self.data_hora_inicio}'
