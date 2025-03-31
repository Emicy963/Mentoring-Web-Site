from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

def register_view(request):
    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if not password == password_confirm:
            return redirect('register')
        
        if len(password):
            return redirect('register')
        
        users = User.objects.filter(username=name)

        if users.exists():
            return redirect('register')
        
        user = User.objects.create_user(
            username=name,
            password=password
        )
        login(request, user)

        return redirect('home')
