from django.shortcuts import render, redirect
from .models import Navigators, Mentees
from django.contrib import messages
from django.contrib.messages import constants

def mentees_views(request):
    if request.method=='GET':
        navigators = Navigators.objects.filter(user=request.user)
        mentees = Mentees.objects.filter(user=request.user)
        return render(request, 'mentees.html', {'stages': Mentees.choice_stage, 'navigators': navigators, 'mentees': mentees})
    elif request.method=='POST':
        name = request.POST.get('name')
        photo = request.POST.get('photo')
        stage = request.POST.get('stage')
        navigator = request.POST.get('navigator')
        try:
            mentees = Mentees(
                name=name,
                photo=photo,
                stage=stage,
                navigator=navigator,
                user=request.user
            )

            mentees.save()

            messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso!')
            return redirect('mentees')
        except Exception as err:
            messages.add_message(request, constants.ERROR, f'Erro ao cadastrar mentorado: {str(err)}')
            return redirect('mentees')
