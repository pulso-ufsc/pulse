from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdminChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        field_classes = {"email": forms.EmailField}


class UserAdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {"email": forms.EmailField}
        error_messages = {
            "email": {
                "unique": _("Esse e-mail já está em uso."),
            }
        }

    def validate_passwords(
        self,
        password1_field_name="password1",
        password2_field_name="password2",
    ):
        password1 = self.cleaned_data.get(password1_field_name)
        password2 = self.cleaned_data.get(password2_field_name)

        if password1 and password2 and password1 != password2:
            error = ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
            self.add_error(password2_field_name, error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_unusable_password()
        if commit:
            user.save()
        return user
