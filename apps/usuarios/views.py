from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            nome_usuario = form['nome_login'].value()
            senha_usuario = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome_usuario,
                password=senha_usuario,
            )

            if usuario:
                auth.login(request, usuario)
                messages.success(request, f'Bem-Vindo {nome_usuario}!')
                return redirect('index')
            else:
                messages.error(request, 'Não foi possível efetuar login!')
                return redirect('login')


    return render(request, 'usuarios/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

def cadastro(request):
    form = CadastroForm()
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form['senha1'].value() != form['senha2'].value():
                messages.error(request, 'As senhas não são iguais!')
                return redirect('cadastro')
            
            nome_usuario = form['nome_cadastro'].value()
            email_usuario = form['email'].value()
            senha_usuario = form['senha1'].value()

            if User.objects.filter(username=nome_usuario).exists():
                messages.error('Usuário ja existe')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome_usuario,
                email=email_usuario,
                password=senha_usuario,
            )

            usuario.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form':form})

