from django.db import models


class Macroeconomia(models.Model):
    macroeconomia_ano = models.DateField(null=True, blank=True)
    preco_zn = models.FloatField(null=True, blank=True, default=0)
    preco_pb = models.FloatField(null=True, blank=True, default=0)
    preco_cu = models.FloatField(null=True, blank=True, default=0)
    preco_ag = models.FloatField(null=True, blank=True, default=0)
    preco_au = models.FloatField(null=True, blank=True, default=0)
    tc_zn = models.FloatField(null=True, blank=True, default=0)
    tc_pb = models.FloatField(null=True, blank=True, default=0)
    tc_cu = models.FloatField(null=True, blank=True, default=0)


class Impostos(models.Model):
    imposto_ano = models.DateField(null=True, blank=True)
    income_tax = models.FloatField(null=True, blank=True, default=0)
    participation_tax = models.FloatField(null=True, blank=True, default=0)
    operational_margin_peru_tax = models.FloatField(null=True, blank=True, default=0)
    regalias_mineras_peru_tax = models.FloatField(null=True, blank=True, default=0)
    iem = models.FloatField(null=True, blank=True, default=0)
    gem = models.FloatField(null=True, blank=True, default=0)


class Projeto(models.Model):
    pass


class Capex(models.Model):
    ano = models.DateField(null=True, blank=True)
    pass


class Tir(models.Model):
    pass


