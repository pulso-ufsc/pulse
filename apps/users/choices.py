from django.db import models
from django.utils.translation import gettext_lazy as _


class UserTypes(models.TextChoices):
    ADMIN = "ADMIN", _("Administrador")
    MEDICO = "MEDICO", _("Médico")
    MEMBRO_EQUIPE = "MEMBRO_EQUIPE", _("Membro de Equipe")
    PACIENTE = "PACIENTE", _("Paciente")
