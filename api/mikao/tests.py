# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Treatment
from django.test import TestCase

# Create your tests here.

class TreatmentTestCase(TestCase):
    def setUp(self):
        Treatment.objects.create(name="Oreilles", description="Calme également les troubles au niveau du nez et les douleurs de la gorge.")
        Treatment.objects.create(name="Yeux", description="Éclaircit les yeux, calme l’esprit, évacue la chaleur de la tête.")

    def test_treatments_description(self):
        """Test getDescription() Treatment function"""
        ears = Treatment.objects.get(name="Oreilles")
        eyes = Treatment.objects.get(name="Yeux")
        self.assertEqual(ears.getDescription(), "Calme également les troubles au niveau du nez et les douleurs de la gorge.")
        self.assertEqual(eyes.getDescription(), "Éclaircit les yeux, calme l’esprit, évacue la chaleur de la tête.")