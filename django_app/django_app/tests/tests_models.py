# En tu_app/tests/test_models.py
from django.test import TestCase
from django_app.models import Post
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

class PostModelTestCase(TestCase):
    def setUp(self):
        # Crear un Post para usar en las pruebas
        self.post = Post.objects.create(
            title="Ejemplo de Título",
            content="Contenido de ejemplo",
            pub_date=timezone.now(),
        )

    def test_post_str(self):
        # Verificar que el método __str__ devuelve el título del Post
        self.assertEqual(str(self.post), "Ejemplo de Título")
