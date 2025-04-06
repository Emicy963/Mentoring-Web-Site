from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import ScheduleAvailability, Meetings
from django.contrib import messages
from django.contrib.messages import constants
from mentees.auth import validate_token

def meeting_view(request):
    if request.method=='GET':
        return render(request, 'meentings.html')
    else:
        date = request.POST.get('date')

        date = datetime.strptime(date, '%Y-%m-%dT%H:%M')

        availability = ScheduleAvailability.objects.filter(
            start_date_gte=(date - timedelta(minutes=50)),
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
    
def choose_day(request):
    if not validate_token(request.COOKIES.get('auth_token')):
        return redirect('auth_mentees')
    if request.method=='GET':
        availabilities = ScheduleAvailability.objects.filter(
            start_date_gte=datetime.now(),
            scheduled=False,
        ).values_list('start_date', flat=True)
        opening_hours = []
        for i in availabilities:
            opening_hours.append(i.date().strftime('%d-%m-%Y'))

        return render(request, 'choose_day.html', {'opening_hours': list(set(opening_hours))})
    
def schedule_meeting(request):
    if not validate_token(request.COOKIES.get('auth_token')):
        return redirect('auth_mentees')
    if request.method=='GET':
        date = request.GET.get('date')
        date = datetime.strptime(date, '%d-%m-%Y')
        opening_hours = ScheduleAvailability.objects.filter(
            start_date__gte=date,
            start_date__lt=date + timedelta(days=1),
            scheduled=False
        )
        return render(request, 'schedule_meeting.html', {'opening_hours': opening_hours, 'tags': Meetings.tag_choice})
