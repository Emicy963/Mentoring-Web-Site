from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from mentees.models import Mentees

class ScheduleAvailability(models.Model):
    start_date = models.DateTimeField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.start_date + timedelta(minutes=50)
    
class Meetings(models.Model):
    tag_choice = (
        ('G', 'Gestão'),
        ('M', 'Marketing'),
        ('RH', 'Gestão de Pessoas'),
        ('I', 'Impostos')
    )

    date = models.ForeignKey(ScheduleAvailability, on_delete=models.CASCADE)
    mentees = models.ForeignKey(Mentees, on_delete=models.CASCADE)
    tag = models.CharField(max_length=2, choices=tag_choice)
    descripton = models.TextField()
