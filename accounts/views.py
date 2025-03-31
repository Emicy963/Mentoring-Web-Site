from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register_view(request):
    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if not password == password_confirm:
            messages.error(request, 'Password diferentes. Tente novamente.')
            return redirect('register')
        
        if len(password):
            messages.error(request, 'A senha deve ter ao menos 6 caracteres.')
            return redirect('register')

        if User.objects.filter(username=name).exists():
            return redirect('register')
        
        try:
            User.objects.create_user(
                username=name,
                password=password
            )

            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Usuário criado com sucesso.')
                return redirect('home')
            else:
                messages.error(request, 'Erro ao autenticar usuário.')
                return redirect('home')
        except Exception as err:
            messages.error(request, f'Erro ao criar usuário: {str(err)}')
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
            return redirect('home')

        messages.error(request, 'Username ou senha errada!')
        return redirect('login')
