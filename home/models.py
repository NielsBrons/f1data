from django.urls import reverse
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import PositiveSmallIntegerField
from django.db.models import SmallIntegerField
from django.db.models import TimeField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models



class Races(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    season = models.PositiveSmallIntegerField()
    round = models.SmallIntegerField() # got to refactor field name
    sprint = models.BooleanField()

    circuit = models.ForeignKey(
        'home.Circuit',
        on_delete=models.CASCADE, related_name="races",
    )


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_races_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_races_update', args=(self.pk,))


class Events(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    date = models.DateField()
    time = models.TimeField()
    
    RACE = 'RACE'
    QUALIFYING = 'QUAL'
    PRACTICE1 = 'P1'
    PRACTICE2 = 'P2'
    PRACTICE3 = 'P3'
    SPRINT = 'SPRT'
    TYPE_CHOICES = [
        (RACE, 'Race'),
        (QUALIFYING, 'Qualifying'),
        (PRACTICE1, 'Practice 1'),
        (PRACTICE2, 'Practice 2'),
        (PRACTICE3, 'Practice 3'),
        (SPRINT, 'Sprint'),
    ]
    
    type = models.CharField(
        max_length=4,
        choices=TYPE_CHOICES,
    )


    # Relationship Fields
    race = models.ForeignKey(
        'home.Races',
        on_delete=models.CASCADE, related_name="events", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_events_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_events_update', args=(self.pk,))


class Circuit(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    country = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('home_circuit_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('home_circuit_update', args=(self.pk,))
    
class Driver(models.Model):
    
    # Fields
    name = models.CharField(max_length=225)
    number = models.SmallIntegerField()
    permanent_number = models.SmallIntegerField()
    team = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
class Point(models.Model):
    
    # Fields
    points = models.SmallIntegerField()
    season = models.PositiveSmallIntegerField()
    eliminated = models.BooleanField()
    max_points = models.SmallIntegerField()
    
    # Relationship Fields
    driver = models.ForeignKey(
        'home.driver',
        on_delete=models.CASCADE, related_name="driver", 
    )
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
class Results(models.Model):
    points = models.SmallIntegerField()
    total_time = models.DurationField()
    fastest_lap = models.DurationField()
    position = models.SmallIntegerField()
    
    event = models.ForeignKey(
        'home.events',
        on_delete=models.CASCADE, related_name="events", 
    )
    
    driver = models.ForeignKey(
        'home.driver',
        on_delete=models.CASCADE, related_name="driver", 
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


class PointMath(models.Model):
    season = models.PositiveSmallIntegerField()
    max_points = models.PositiveSmallIntegerfield()
    points_left = models.PositiveSmallIntegerfield()
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
