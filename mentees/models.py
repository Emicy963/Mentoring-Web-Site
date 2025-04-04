import secrets
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
    token = models.CharField(max_length=16, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_unique_token()
        super().save(*args, **kwargs)

    def generate_unique_token(self):
        while True:
            token = secrets.token_urlsafe(8)
            if not Mentees.objects.filter(token=token).exists():
                return token

    def __str__(self):
        return self.name
