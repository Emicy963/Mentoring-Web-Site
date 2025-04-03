from django.test import TestCase
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

    def test_mentees_view_get(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('mentees'))
        self.assertEqual(response.status_code, 200)

    def test_mentees_view_post(self):
        user = User.objects.create_user(username='testuser', password='12345')
        navigator = Navigators.objects.create(name='Navigator 1', user=user)
        self.client.login(username='testuser', password='12345')

        response = self.client.post(reverse('mentees'), {
            'name': 'Mentee Test',
            'stage': 'E1',
            'navigator': navigator.id,
        })
        self.assertEqual(Mentees.objects.count(), 1)
        self.assertEqual(Mentees.objects.first().name == 'Mentee Test')
