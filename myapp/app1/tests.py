from django.test import TestCase
from app1.models import Adresses, Genre


class TestAdresses(TestCase):
    """Tester la relation one-to-many"""
    def test_up(self):

        m = Genre.objects.create(genre="M")
        f = Genre.objects.create(genre="F")

        Adresses.objects.create(prenom = 'rené',
                                nom = 'dylan',
                                tel = 963,
                                genre = m
                                )
        
        res = Adresses.objects.get(prenom='rené')
        self.assertEqual(res.genre.genre, 'M')

