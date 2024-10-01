import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.validators import CPFValidator

from .choices import UserTypes
from .managers import UserManager


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name=_("ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(
        verbose_name=_("Nome"),
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name=_("Sobrenome"),
        max_length=50,
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("Ativo"),
        default=True,
        help_text=_("Desmarque para desativar a conta ao invés de excluí-la."),
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff"),
        default=False,
        help_text=_("Garante acesso ao painel administrativo do Django."),
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Superusuário"),
        default=False,
        help_text=_("Atribui todos os direitos e permissões possíveis."),
    )
    date_joined = models.DateTimeField(
        verbose_name=_("Data de cadastro"),
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name=_("Último acesso"),
        auto_now=True,
    )
    username = None

    cpf = models.CharField(
        verbose_name=_("CPF"),
        max_length=11,
        unique=True,
        validators=[CPFValidator()],
    )
    type = models.CharField(
        verbose_name=_("Tipo de Usuário"),
        max_length=13,
        choices=UserTypes.choices,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "cpf", "type"]

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    def __str__(self):
        return f"{self.get_full_name()} ({self.cpf_formatado})"

    def clean(self):
        super().clean()
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.is_staff = True if self.is_superuser else self.is_staff

    @property
    def cpf_formatado(self):
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
