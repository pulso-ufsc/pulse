from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (
            _("Credenciais de login"),
            {
                "fields": (
                    "email",
                    "cpf",
                    "type",
                    "password",
                )
            },
        ),
        (
            _("Informações pessoais"),
            {
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissões"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Datas importantes"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            _("Credenciais de login"),
            {
                "fields": (
                    "email",
                    "cpf",
                    "type",
                ),
            },
        ),
        (
            _("Informações pessoais"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )
    list_display = (
        "cpf_formatado",
        "first_name",
        "last_name",
        "email",
        "type",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )
    list_filter = (
        "type",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "email",
        "cpf",
        "first_name",
        "last_name",
    )
    ordering = (
        "first_name",
        "last_name",
    )
    readonly_fields = (
        "id",
        "last_login",
        "date_joined",
    )
    list_per_page = 10
