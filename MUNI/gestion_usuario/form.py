from django.forms import ModelForm
from .models import Funcionario

#creando el formulario para el modelo Funcionario 
class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nombre', 'apellido', 'correo', 'telfono', 'perfil']