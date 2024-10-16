from django.db import models
"""
Adicionar um metodo no admin para duplicar o obketo que eh base case
e entao slvar ele com is_base_case False."""
"""se usar property, nao eh necessario criar duplicacao com alteracao
das variavies pois elas podem ser acessadas
dinamicamente sem serem armazenadas"""


class Projeto(models.Model):
    """novo_closure = models.IntegerField(null=True, blank=True, default=0)
    alteracao_initial_capex_percentual = models.FloatField(
        null=True, blank=True, default=0)
    alteracao_mining_cost_percentual = models.FloatField(
        null=True, blank=True, default=0)
    alteracao_mill_percentual = models.FloatField(
        null=True, blank=True, default=0)
    alteracao_ore_percentual = models.FloatField(
        null=True, blank=True, default=0)
    alteracao_recovery_percentual = models.FloatField(
        null=True, blank=True, default=0)
    alteracao_grade_percentual = models.FloatField(
        null=True, blank=True, default=0)
    alteracao_processing_cost_percentual = models.FloatField(
        null=True, blank=True, default=0)
    is_base_case = models.BooleanField(default=True)"""
    nome = models.CharField(max_length=40, blank=True, null=True)
    first_capex = models.IntegerField(null=True, blank=True, default=0)
    last_capex = models.IntegerField(null=True, blank=True, default=0)
    start_up = models.IntegerField(null=True, blank=True, default=0)
    closure = models.IntegerField(null=True, blank=True, default=0)
    capex_implementation = models.FloatField(null=True, blank=True, default=0)
    capex_sustaining = models.FloatField(null=True, blank=True, default=0)
    mill = models.FloatField(null=True, blank=True, default=0)
    mining_cost = models.FloatField(null=True, blank=True, default=0)
    processing_cost = models.FloatField(null=True, blank=True, default=0)
    ga = models.FloatField(null=True, blank=True, default=0)
    rr = models.FloatField(null=True, blank=True, default=0)
    zn_grade = models.FloatField(null=True, blank=True, default=0)
    pb_grade = models.FloatField(null=True, blank=True, default=0)
    cu_grade = models.FloatField(null=True, blank=True, default=0)
    ag_grade = models.FloatField(null=True, blank=True, default=0)
    au_grade = models.FloatField(null=True, blank=True, default=0)
    recovery_pb_zn = models.FloatField(null=True, blank=True, default=0)
    recovery_pb_pb = models.FloatField(null=True, blank=True, default=0)
    recovery_pb_cu = models.FloatField(null=True, blank=True, default=0)
    recovery_pb_ag = models.FloatField(null=True, blank=True, default=0)
    recovery_pb_au = models.FloatField(null=True, blank=True, default=0)
    recovery_zn_zn = models.FloatField(null=True, blank=True, default=0)
    recovery_zn_pb = models.FloatField(null=True, blank=True, default=0)
    recovery_zn_cu = models.FloatField(null=True, blank=True, default=0)
    recovery_zn_ag = models.FloatField(null=True, blank=True, default=0)
    recovery_zn_au = models.FloatField(null=True, blank=True, default=0)
    recovery_cu_zn = models.FloatField(null=True, blank=True, default=0)
    recovery_cu_pb = models.FloatField(null=True, blank=True, default=0)
    recovery_cu_cu = models.FloatField(null=True, blank=True, default=0)
    recovery_cu_ag = models.FloatField(null=True, blank=True, default=0)
    reovery_cu_au = models.FloatField(null=True, blank=True, default=0)
    zn_concentrate_grade = models.FloatField(null=True, blank=True, default=0)
    zn_moinsture = models.FloatField(null=True, blank=True, default=0)
    pb_concentrate_grade = models.FloatField(null=True, blank=True, default=0)
    pb_moinsture = models.FloatField(null=True, blank=True, default=0)
    cu_concentrate_grade = models.FloatField(null=True, blank=True, default=0)
    cu_moinsture = models.FloatField(null=True, blank=True, default=0)

    @property
    def lom(self):
        return (self.closure - self.start_up) + 1

    def __str__(self):
        return self.nome


class Variavel(models.Model):
    """is_base_case = models.BooleanField(default=True)
    alteracao_LME_percentual = models.FloatField(
        null=True, blank=True, default=0)"""
    ano = models.IntegerField(null=True, blank=True)
    zn_price = models.FloatField(null=True, blank=True, default=0)
    pb_price = models.FloatField(null=True, blank=True, default=0)
    cu_price = models.FloatField(null=True, blank=True, default=0)
    ag_price = models.FloatField(null=True, blank=True, default=0)
    au_price = models.FloatField(null=True, blank=True, default=0)
    zn_tc = models.FloatField(null=True, blank=True, default=0)
    pb_tc = models.FloatField(null=True, blank=True, default=0)
    cu_tc = models.FloatField(null=True, blank=True, default=0)

    @property
    def zn_price_mais_5(self):
        return self.zn_price * 1.05

    @property
    def zn_price_mais_10(self):
        return self.zn_price * 1.10

    @property
    def zn_price_mais_15(self):
        return self.zn_price * 1.15

    @property
    def zn_price_mais_20(self):
        return self.zn_price * 1.20

    @property
    def zn_price_menos_5(self):
        return self.zn_price * 0.95

    @property
    def zn_price_menos_10(self):
        return self.zn_price * 0.90

    @property
    def zn_price_menos_15(self):
        return self.zn_price * 0.85

    @property
    def zn_price_menos_20(self):
        return self.zn_price * 0.80

    @property
    def pb_price_mais_5(self):
        return self.pb_price * 1.05

    @property
    def pb_price_mais_10(self):
        return self.pb_price * 1.10

    @property
    def pb_price_mais_15(self):
        return self.pb_price * 1.15

    @property
    def pb_price_mais_20(self):
        return self.pb_price * 1.20

    @property
    def pb_price_menos_5(self):
        return self.pb_price * 0.95

    @property
    def pb_price_menos_10(self):
        return self.pb_price * 0.90

    @property
    def pb_price_menos_15(self):
        return self.pb_price * 0.85

    @property
    def pb_price_menos_20(self):
        return self.pb_price * 0.80

    @property
    def cu_price_mais_5(self):
        return self.cu_price * 1.05

    @property
    def cu_price_mais_10(self):
        return self.cu_price * 1.10

    @property
    def cu_price_mais_15(self):
        return self.cu_price * 1.15

    @property
    def cu_price_mais_20(self):
        return self.cu_price * 1.20

    @property
    def cu_price_menos_5(self):
        return self.cu_price * 0.95

    @property
    def cu_price_menos_10(self):
        return self.cu_price * 0.90

    @property
    def cu_price_menos_15(self):
        return self.cu_price * 0.85

    @property
    def cu_price_menos_20(self):
        return self.cu_price * 0.80

    @property
    def ag_price_mais_5(self):
        return self.ag_price * 1.05

    @property
    def ag_price_mais_10(self):
        return self.ag_price * 1.10

    @property
    def ag_price_mais_15(self):
        return self.ag_price * 1.15

    @property
    def ag_price_mais_20(self):
        return self.ag_price * 1.20

    @property
    def ag_price_menos_5(self):
        return self.ag_price * 0.95

    @property
    def ag_price_menos_10(self):
        return self.ag_price * 0.90

    @property
    def ag_price_menos_15(self):
        return self.ag_price * 0.85

    @property
    def ag_price_menos_20(self):
        return self.ag_price * 0.80

    @property
    def au_price_mais_5(self):
        return self.au_price * 1.05

    @property
    def au_price_mais_10(self):
        return self.au_price * 1.10

    @property
    def au_price_mais_15(self):
        return self.au_price * 1.15

    @property
    def au_price_mais_20(self):
        return self.au_price * 1.20

    @property
    def au_price_menos_5(self):
        return self.au_price * 0.95

    @property
    def au_price_menos_10(self):
        return self.au_price * 0.90

    @property
    def au_price_menos_15(self):
        return self.au_price * 0.85

    @property
    def au_price_menos_20(self):
        return self.au_price * 0.80

    @property
    def zn_tc_mais_5(self):
        return self.zn_tc * 1.05

    @property
    def zn_tc_mais_10(self):
        return self.zn_tc * 1.10

    @property
    def zn_tc_mais_15(self):
        return self.zn_tc * 1.15

    @property
    def zn_tc_mais_20(self):
        return self.zn_tc * 1.20

    @property
    def zn_tc_menos_5(self):
        return self.zn_tc * 0.95

    @property
    def zn_tc_menos_10(self):
        return self.zn_tc * 0.90

    @property
    def zn_tc_menos_15(self):
        return self.zn_tc * 0.85

    @property
    def zn_tc_menos_20(self):
        return self.zn_tc * 0.80

    @property
    def pb_tc_mais_5(self):
        return self.pb_tc * 1.05

    @property
    def pb_tc_mais_10(self):
        return self.pb_tc * 1.10

    @property
    def pb_tc_mais_15(self):
        return self.pb_tc * 1.15

    @property
    def pb_tc_mais_20(self):
        return self.pb_tc * 1.20

    @property
    def pb_tc_menos_5(self):
        return self.pb_tc * 0.95

    @property
    def pb_tc_menos_10(self):
        return self.pb_tc * 0.90

    @property
    def pb_tc_menos_15(self):
        return self.pb_tc * 0.85

    @property
    def pb_tc_menos_20(self):
        return self.pb_tc * 0.80

    @property
    def cu_tc_mais_5(self):
        return self.cu_tc * 1.05

    @property
    def cu_tc_mais_10(self):
        return self.cu_tc * 1.10

    @property
    def cu_tc_mais_15(self):
        return self.cu_tc * 1.15

    @property
    def cu_tc_mais_20(self):
        return self.cu_tc * 1.20

    @property
    def cu_tc_menos_5(self):
        return self.cu_tc * 0.95

    @property
    def cu_tc_menos_10(self):
        return self.cu_tc * 0.90

    @property
    def cu_tc_menos_15(self):
        return self.cu_tc * 0.85

    @property
    def cu_tc_menos_20(self):
        return self.cu_tc * 0.80

    def __str__(self):
        return self.ano


class CashFlow(models.Model):
    projeto = models.ForeignKey(
        Projeto, on_delete=models.SET_NULL, blank=True, null=True)
    variavel = models.ForeignKey(
        Variavel, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.projeto.nome


class Tir(models.Model):
    cashflow = models.ForeignKey(
        CashFlow, on_delete=models.SET_NULL, blank=True, null=True)
    tir = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return self.TIR
