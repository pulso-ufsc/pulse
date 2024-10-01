from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import EstadosBrasil


class EnderecoMixin(models.Model):
    cep = models.CharField(
        verbose_name=_("CEP"),
        max_length=8,
        validators=[
            RegexValidator(
                regex=r"^\d{8}$",
                message=_("CEP deve conter 8 dígitos."),
            )
        ],
    )
    estado = models.CharField(
        verbose_name=_("Estado"),
        max_length=2,
        choices=EstadosBrasil.choices,
    )
    cidade = models.CharField(
        verbose_name=_("Cidade"),
        max_length=255,
    )
    bairro = models.CharField(
        verbose_name=_("Bairro"),
        max_length=255,
    )
    logradouro = models.CharField(
        verbose_name=_("Logradouro"),
        max_length=255,
    )
    numero = models.CharField(
        verbose_name=_("Número"),
        max_length=5,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\w{1,5}$",
                message=_("Número deve conter até 5 caracteres."),
            )
        ],
    )
    complemento = models.CharField(
        verbose_name=_("Complemento"),
        max_length=255,
        blank=True,
    )

    class Meta:
        abstract = True

    @property
    def cep_formatado(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
