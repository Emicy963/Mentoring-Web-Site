from django.db import models
from django.contrib.auth.models import User

class Navigators(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Mentees(models.Model):
    choice_stage = (
        ('E1', '10-100k'),
        ('E2', '100-1kk')
    )
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    stage = models.CharField(max_length=2, choices=choice_stage)
    navigator = models.ForeignKey(Navigators, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
