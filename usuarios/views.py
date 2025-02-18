from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')