from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from usuarios.models import Administrador
from getpass import getpass


class Command(BaseCommand):
    help = 'Utilidad para crear nuevos administradores'

    def handle(self, *args, **options):
        mail = input('Email: ')
        name = input('Nombre: ')
        lname = input('Apellido: ')
        password = getpass('Contraseña: ')
        user = User.objects.create_user(username=mail, password=password)

        admin_group, _ = Group.objects.get_or_create(name='administradores')
        user.groups.add(admin_group)

        administrador = Administrador(
            user=user,
            nombre=name,
            apellido=lname,
        )
        administrador.save()
        self.stdout.write(self.style.SUCCESS('Listo!'))


