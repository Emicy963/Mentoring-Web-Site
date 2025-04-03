from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import ScheduleAvailability, Meetings
from django.contrib import messages
from django.contrib.messages import constants

def meeting_view(request):
    if request.method=='GET':
        return render(request, 'meentings.html')
    else:
        date = request.POST.get('date')

        date = datetime.strptime(date, '%Y-%m-%dT%H:%M')

        availability = ScheduleAvailability.objects.filter(
            start_date_gte=(date - timedelta(minutes=50))
            start_date_lte=(date + timedelta(minutes=50))
        )

        if availability.exists():
            messages.add_message(request, constants.ERROR, 'Você já possui uma reunião aberta!')
            return redirect('meetings')
        
        availability = ScheduleAvailability(
            start_date=date,
            meentor=request.user
        )
        availability.save()

        messages.add_message(request, constants.SUCCESS, 'Horário disponibilizado com sucesso.')
        return redirect('meetings')
