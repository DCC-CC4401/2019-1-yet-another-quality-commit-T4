from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from usuarios.models import Administrador
from getpass import getpass


class Command(BaseCommand):
    help = 'Utilidad para crear nuevos administradores'

    def handle(self, *args, **options):
        username = input('Nombre de usuario: ')
        mail = input('Email: ')
        password = getpass('Contraseña: ')
        user = User.objects.create_user(username, mail, password)

        admin_group = Group.objects.get_or_create(name='administradores')
        user.groups.add(admin_group)

        administrador = Administrador(user=user)
        administrador.save()
        self.stdout.write(self.style.SUCCESS('Listo!'))


