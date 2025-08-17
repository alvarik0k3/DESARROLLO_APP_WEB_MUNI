from django.shortcuts import render
from .models import Funcionario
from .form  import FuncionarioForm

# Create your views here.

def index(request):
    context ={}
    form = FuncionarioForm()
    funcionario = Funcionario.objects.all()
    context['funcionario'] = funcionario
    if request.method == "POST":
        if 'Save' in request.POST:
            pk= request.POST.get('Save')
            if not pk:
                form = FuncionarioForm(request.POST)
                
            else:
                funcionario = Funcionario.objects.get(id=pk)
                form = FuncionarioForm(request.POST, instance=funcionario)
            form.save()
            form = FuncionarioForm()
        elif 'Delete' in request.POST:
            pk= request.POST.get('Delete')
            funcionario = Funcionario.objects.get(id=pk)
            funcionario.delete()
        elif 'Edit' in request.POST:
            pk= request.POST.get('Edit')
            funcionario = Funcionario.objects.get(id=pk)
            form = FuncionarioForm(instance=funcionario)
            funcionario = form
    context['form'] = form
    return render(request, 'gestion_usuario/index.html', context)