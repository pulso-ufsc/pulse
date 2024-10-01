from django.core.management.base import BaseCommand

from ...models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        default_password = "2305"
        test_users = [
            {
                "first_name": "Dennis",
                "last_name": "Paz",
                "email": "dppazlopez@gmail.com",
                "is_active": True,
                "is_staff": True,
                "is_superuser": True,
                "cpf": "01234491974",
                "type": "ADMIN",
            },
        ]

        for test_user in test_users:
            obj, created = User.objects.update_or_create(
                email=test_user["email"],
                defaults={**test_user},
            )
            if created:
                obj.set_password(default_password)
                obj.save(update_fields=["password"])
                self.stdout.write(self.style.SUCCESS(f"User {obj} created"))
