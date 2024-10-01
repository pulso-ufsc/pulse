import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class CPFValidator:
    message = _("CPF inválido.")
    code = "invalid_cpf"

    def __call__(self, value):
        cpf = re.sub(r"[^0-9]", "", value)
        if len(cpf) != 11 or cpf == cpf[0] * 11 or not self.validate(cpf):
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return isinstance(other, CPFValidator)

    def validate(self, cpf):
        for i in range(9, 11):
            if self.calculate_digit(cpf, i) != int(cpf[i]):
                return False
        return True

    def calculate_digit(self, cpf, digit):
        result = sum(int(cpf[i]) * (digit + 1 - i) for i in range(digit))
        result = result % 11
        return 0 if result < 2 else 11 - result
