from django.shortcuts import render
from .models import Funcionario
from .form  import FuncionarioForm

# Create your views here.

def index(request):
    context ={}
    form = FuncionarioForm()
    funcionario = Funcionario.objects.all()
    context['funcionario'] = funcionario
    context['form'] = form
    return render(request, 'gestion_usuario/index.html', context)