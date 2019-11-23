# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    #email = models.EmailField(max_length = 254) 
 
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
 
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
 
class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
 
    class Meta:
        verbose_name = "Treatment"
        verbose_name_plural = "Treatments"
 
    def __unicode__(self):
        return self.name

    def getDescription(self):
        return self.description

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    treatments = models.ManyToManyField(Treatment, verbose_name="list of treatments")
    
    #university = models.ForeignKey(University, on_delete=models.DO_NOTHING)
 
    class Meta:
        verbose_name = "Symptom"
        verbose_name_plural = "Symptoms"
 
    def __unicode__(self):
        return self.name

class FavoriteList(models.Model):
    symptoms = models.ManyToManyField(Symptom, verbose_name="list of symptoms")
    treatments = models.ManyToManyField(Treatment, verbose_name="list of treatments")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, related_name='favoriteLists', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "FavoriteList"
        verbose_name_plural = "FavoriteLists"
 
    def __unicode__(self):
        return self