from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça Login primeiro!')
        return redirect('login')

    fotografias = Fotografia.objects.filter(publicado=True).order_by('-data_fotografia')
    return render(request, 'galeria/index.html', {"cards":fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça Login primeiro!')
        return redirect('login')

    fotografias = Fotografia.objects.filter(publicado=True).order_by('-data_fotografia')
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    
    return render (request, 'galeria/buscar.html', {'cards':fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça Login primeiro!')
        return redirect('login')

    form = FotografiaForm()

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia cadastrada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request):
    pass

def remover_imagem(request):
    pass