from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.messages import constants

def register_view(request):
    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if not password == password_confirm:
            messages.add_message(request, constants.ERROR , 'Password diferentes. Tente novamente.')
            return redirect('register')
        
        if len(password):
            messages.add_message(request, constants.ERROR, 'A senha deve ter ao menos 6 caracteres.')
            return redirect('register')

        if User.objects.filter(username=name).exists():
            messages.add_message(request, constants.ERROR, 'Este usuário já está registrado')
            return redirect('register')
        
        try:
            User.objects.create_user(
                username=name,
                password=password
            )

            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)
                messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso.')
                return redirect('home')
            else:
                messages.add_message(request, constants.ERROR, 'Erro ao autenticar usuário.')
                return redirect('home')
        except Exception as err:
            messages.add_message(request,constants.ERROR, f'Erro ao criar usuário: {str(err)}')
            return redirect('register')
    
def login_view(request):
    if request.method=='GET':
        return render(request, 'login.html')
    elif request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Login feito com sucesso.')
            return redirect('home')

        messages.add_message(request, constants.ERROR, 'Username ou senha errada!')
        return redirect('login')
