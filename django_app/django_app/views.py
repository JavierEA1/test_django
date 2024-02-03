# En django_app/views.py
from django.shortcuts import render
from .forms import MiFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm
# En tu_app/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
def index(request):
    return render(request, 'index.html')

def formulario_view(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            # Procesar los datos del formulario si es válido
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['mensaje']
            print(f"Nombre: {nombre}, Email: {email}, Mensaje: {mensaje}")
            # Hacer algo con los datos (guardar en la base de datos, enviar por correo, etc.)
        else:
            # El formulario no es válido, manejar de acuerdo a tus necesidades
            errores = formulario.errors
            # Puedes hacer algo con los errores, como imprimirlos en la consola o enviarlos a la plantilla
            print(errores)
    else:
        formulario = MiFormulario()

    return render(request, 'formulario.html', {'formulario': formulario})

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vista_protegida')  # Redirige a la vista protegida después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registro_usuario.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')  


class RegistroUsuarioView(CreateView):
    template_name = 'registro_usuario.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('nombre_de_la_ruta_de_inicio')  # Ajusta con la ruta de inicio

    def form_valid(self, form):
        response = super().form_valid(form)
        # Puedes realizar acciones adicionales aquí si es necesario
        return response

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # urls.py
