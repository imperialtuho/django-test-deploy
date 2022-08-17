from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Common(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=255)
    type = models.CharField(max_length=32)
    armament = ArrayField(models.CharField(
        max_length=64, blank=True), default=list)
    equipment = ArrayField(models.CharField(
        max_length=64, blank=True), default=list)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tank(Common):
    feature = models.CharField(max_length=255)


class Aircraft(Common):
    feature = models.CharField(max_length=255)


class Helicopter(Common):
    feature = models.CharField(max_length=255)


class Battleship(Common):
    feature = models.CharField(max_length=255)


class Crew(Common):
    expertise = models.CharField(max_length=64)
