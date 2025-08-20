from django.forms import ModelForm
from .models import Usuario

#creando el formulario para el modelo Usuario
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'telfono', 'perfil']