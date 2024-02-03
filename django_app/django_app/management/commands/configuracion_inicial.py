# En your_app/management/commands/configuracion_inicial.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from models import Post
class Command(BaseCommand):
    help = 'Configuración inicial de la aplicación'

    def handle(self, *args, **options):
        # Crear un grupo
        grupo_vistas_limitadas, creado = Group.objects.get_or_create(name='Vistas Limitadas')

        # Obtener el permiso necesario
        content_type = ContentType.objects.get_for_model(Post)  # Sustituye YourModel por el modelo relevante
        permiso_ver_vista_especifica, creado = Permission.objects.get_or_create(
            content_type=content_type,
            codename='puede_ver_vista_especifica'
        )

        # Asignar el permiso al grupo
        grupo_vistas_limitadas.permissions.add(permiso_ver_vista_especifica)

        # Crear un usuario
        usuario, creado = User.objects.get_or_create(username='nombre_de_usuario')
        usuario.set_password('contrasena')  # Cambia 'contrasena' por la contraseña que desees
        usuario.save()

        # Asignar usuario al grupo de vistas limitadas
        usuario.groups.add(grupo_vistas_limitadas)

        self.stdout.write(self.style.SUCCESS('Configuración inicial completada con éxito.'))
