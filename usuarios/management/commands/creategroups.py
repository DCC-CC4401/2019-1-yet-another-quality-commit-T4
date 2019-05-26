from django.core.management.base import BaseCommand
from django.contrib.auth.models import  Group

class Command(BaseCommand):
    help = 'Crea los grupos de usuarios si no existen'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creando grupos'))
        _, a_created = Group.objects.get_or_create(name='administrador')
        _, e_created = Group.objects.get_or_create(name='evaluador')
        if not a_created:
            self.stdout.write(self.style.WARNING('Grupo "administradores" ya existia'))
        if not e_created:
            self.stdout.write(self.style.WARNING('Grupo "evaluadores" ya existia'))
        self.stdout.write(self.style.SUCCESS('Listo!'))