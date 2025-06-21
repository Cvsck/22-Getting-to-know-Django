from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Создаёт группу 'Модератор продуктов' с нужными правами"

    def handle(self, *args, **kwargs):
        moderator_group, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )

        unpublish_permission = Permission.objects.get(codename="can_unpublish_product")
        delete_permission = Permission.objects.get(codename="can_delete_any_product")

        moderator_group.permissions.add(unpublish_permission, delete_permission)

        self.stdout.write(self.style.SUCCESS("Группа 'Модератор продуктов' создана!"))
