from .models import Mentees

def validate_token(token):
    return Mentees.objects.filter(token=token)
