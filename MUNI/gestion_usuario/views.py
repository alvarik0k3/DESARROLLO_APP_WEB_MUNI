from django.shortcuts import render
from .models import Usuario
from .form  import UsuarioForm

# Create your views here.

def index(request):
    context ={}
    form = UsuarioForm()
    usuario = Usuario.objects.all()
    context['usuario'] = usuario
    if request.method == "POST":
        if 'Save' in request.POST:
            pk= request.POST.get('Save')
            if not pk:
                form = UsuarioForm(request.POST)
                
            else:
                usuario = Usuario.objects.get(id=pk)
                form = UsuarioForm(request.POST, instance=usuario)
            form.save()
            form = UsuarioForm()
        elif 'Delete' in request.POST:
            pk= request.POST.get('Delete')
            usuario = Usuario.objects.get(id=pk)
            usuario.delete()
        elif 'Edit' in request.POST:
            pk= request.POST.get('Edit')
            usuario = Usuario.objects.get(id=pk)
            form = UsuarioForm(instance=usuario)
            usuario = form
    context['form'] = form
    return render(request, 'gestion_usuario/index.html', context)