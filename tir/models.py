from django.db import models

# models.CharField(max_length=40, blank=True, null=True)
# models.FloatField(null=True, blank=True, default=0)
# models.ForeignKey(Classe, on_delete=models.SET_NULL, blank=True, null=True)
# models.ManyToManyField(Classe, blank=True)
# models.IntegerField(null=True, blank=True)


class Ano(models.Model):
    ano = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.ano


class Projeto(models.Model): # possivelmente tudo tera que ser default = 0 para evitar que o mesmo calculo seja feito sempre em cada salvacao )
    alteracao_closure_anos = models.IntegerField(null=True, blank=True)
    alteracao_initial_capex_percentual = models.FloatField(null=True, blank=True)
    alteracao_mining_cost_percentual = models.FloatField(null=True, blank=True)
    alteracao_mill_percentual = models.FloatField(null=True, blank=True)
    alteracao_ore_percentual = models.FloatField(null=True, blank=True)
    alteracao_recovery_percentual = models.FloatField(null=True, blank=True)
    alteracao_grade_percentual = models.FloatField(null=True, blank=True)
    alteracao_processing_cost_percentual = models.FloatField(null=True, blank=True)
    is_base_case = models.BooleanField(default=True)
    nome = models.CharField(max_length=40, blank=True, null=True)
    first_capex = models.ForeignKey(Ano, on_delete=models.SET_NULL, blank=True, null=True)
    last_capex = models.ForeignKey(Ano, on_delete=models.SET_NULL, blank=True, null=True)
    start_up = models.ForeignKey(Ano, on_delete=models.SET_NULL, blank=True, null=True)
    closure = models.ForeignKey(Ano, on_delete=models.SET_NULL, blank=True, null=True)
    capex_implementation = models.FloatField(null=True, blank=True)
    capex_sustaining = models.FloatField(null=True, blank=True)
    LOM = models.IntegerField(null=True, blank=True)
    mill = models.FloatField(null=True, blank=True)
    mining_cost = models.FloatField(null=True, blank=True)
    processing_cost = models.FloatField(null=True, blank=True)
    GA = models.FloatField(null=True, blank=True)
    RR = models.FloatField(null=True, blank=True)
    zn_grade = models.FloatField(null=True, blank=True)
    pb_grade = models.FloatField(null=True, blank=True)
    cu_grade = models.FloatField(null=True, blank=True)
    ag_grade = models.FloatField(null=True, blank=True)
    au_grade = models.FloatField(null=True, blank=True)
    recovery_pb_zn = models.FloatField(null=True, blank=True)
    recovery_pb_pb = models.FloatField(null=True, blank=True)
    recovery_pb_cu = models.FloatField(null=True, blank=True)
    recovery_pb_ag = models.FloatField(null=True, blank=True)
    recovery_pb_au = models.FloatField(null=True, blank=True)
    recovery_zn_zn = models.FloatField(null=True, blank=True)
    recovery_zn_pb = models.FloatField(null=True, blank=True)
    recovery_zn_cu = models.FloatField(null=True, blank=True)
    recovery_zn_ag = models.FloatField(null=True, blank=True)
    recovery_zn_au = models.FloatField(null=True, blank=True)
    recovery_cu_zn = models.FloatField(null=True, blank=True)
    recovery_cu_pb = models.FloatField(null=True, blank=True)
    recovery_cu_cu = models.FloatField(null=True, blank=True)
    recovery_cu_ag = models.FloatField(null=True, blank=True)
    reovery_cu_au = models.FloatField(null=True, blank=True)
    zn_concentrate_grade = models.FloatField(null=True, blank=True)
    zn_moinsture = models.FloatField(null=True, blank=True)
    pb_concentrate_grade = models.FloatField(null=True, blank=True)
    pb_moinsture = models.FloatField(null=True, blank=True)
    cu_concentrate_grade = models.FloatField(null=True, blank=True)
    cu_moinsture = models.FloatField(null=True, blank=True)

    def alteracao(self):
        pass

    def calculo(self):
        self.LOM = (self.closure - self.start_up) + 1

    def save(self, *args, **kwargs):
        self.calculo()
        self.alteracao()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Variavel(models.Model): # usar default = 0 caso o calculo se repetir em cada salvada
    is_base_case = models.BooleanField(default=True)
    alteracao_LME_percentual = models.FloatField(null=True, blank=True)
    ano = models.ForeignKey(Ano, on_delete=models.SET_NULL, blank=True, null=True)
    zn_price = models.FloatField(null=True, blank=True)
    pb_price = models.FloatField(null=True, blank=True)
    cu_price = models.FloatField(null=True, blank=True)
    ag_price = models.FloatField(null=True, blank=True)
    au_price = models.FloatField(null=True, blank=True)
    zn_tc = models.FloatField(null=True, blank=True)
    pb_tc = models.FloatField(null=True, blank=True)
    cu_tc = models.FloatField(null=True, blank=True)

    def alteracao(self):
        pass

    def calculo(self):
        pass

    def save(self, *args, **kwargs):
        self.calculo()
        self.alteracao()
        super().save(*args, **kwargs)

    # necessario fazer um metodo no admin para duplicar o objeto e nao ter que preencher do zero o formulario

    def __str__(self):
        return self.ano


class CashFlow(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.SET_NULL, blank=True, null=True)
    variavel = models.ForeignKey(Variavel, on_delete=models.SET_NULL, blank=True, null=True)

    def calculo(self):
        pass

    def save(self, *args, **kwargs):
        self.calculo()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.projeto.nome


class Tir(models.Model):
    cashflow = models.ForeignKey(CashFlow, on_delete=models.SET_NULL, blank=True, null=True)
    TIR = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.TIR
