from django.db import models
from django.utils import timezone

# Create your models here.


class Fornecedor(models.Model):
    nome = models.CharField(max_length=50, null=False,
                            verbose_name="Nome/Razão Social")
    cnpj = models.CharField(max_length=19, null=False, verbose_name="CNPJ",
                            unique=True, help_text="(Formato 99.999.999/9999-99)")
    ddd_telefone = models.CharField(
        max_length=2, verbose_name="DDD", help_text="(Formato 99)")
    telefone = models.CharField(
        max_length=10, verbose_name="Telefone", help_text="(Formato 99999-9999)")
    data_cadastro = models.DateTimeField(
        default=timezone.now, verbose_name="Data criação")

    def __str__(self):
        return self.nome

