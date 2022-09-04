from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=TRUE, blank=True)
    date_of_birth = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    positions = models.ManyToManyField(Position, related_name='positions', blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=1)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name




