from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Common(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=32)
    armament = ArrayField(models.CharField(
        max_length=64, blank=True), default=list)
    equipment = ArrayField(models.CharField(
        max_length=64, blank=True), default=list)
    feature = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tank(Common):
    pass


class Aircraft(Common):
    pass


class Helicopter(Common):
    pass


class Battleship(Common):
    pass


class Crew(Common):
    expertise = models.CharField(max_length=64)
