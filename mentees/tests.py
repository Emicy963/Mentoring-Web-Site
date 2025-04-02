from django.test import TestCase
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Navigators, Mentees

class MenteesTestCase(TestCase):
    def test_navigators_model(self):
        user = User.objects.create_user(username='testuser', password='12345')
        navigator = Navigators.objects.create(name='Navigator 1', user=user)
        self.assertEqual(str(navigator), 'Navigator 1')

    def test_mentees_model(self):
        user = User.objects.create_user(username='testuser', password='12345')
        navigator = Navigators.objects.create(name='Navigator 1', user=user)
        mentee = Mentees.objects.create(name='Mentee 1', stage='E1', navigator=navigator, user=user)
        self.assertEqual(str(mentee), 'Mentee 1')
