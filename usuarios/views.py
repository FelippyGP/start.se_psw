from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

    if not senha == confirmar_senha:
        messages.add_messages(request, constants.ERROR, "senha não corresponde a o confirmar senha")
        return redirect('/usuarios/cadastro')
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR,"senha tem menos de 6 caracteres")
        return redirect('/usuarios/cadastro')
    
    users =User.objects.filter(username=username)

    if users.exists():
        messages.add_messages(request, constants.ERROR,"username não disponivel")
        return redirect('/usuarios/cadastro')
    
    user = User.objects.create_user(
        username=username,
        password=senha
    )
    
    return redirect('/usuarios/login')


def login(request):
    if request.method == "GET" :
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/home')
        
        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
        return redirect('/usuarios/login')
        
        
