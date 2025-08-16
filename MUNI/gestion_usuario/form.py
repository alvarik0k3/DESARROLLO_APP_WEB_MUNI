from django.forms import ModelForm
from .models import Funcionario

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nombre', 'apellido', 'correo', 'telfono', 'perfil']