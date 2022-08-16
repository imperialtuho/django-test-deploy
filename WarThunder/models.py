from django.db import models

# Create your models here.


class Common(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=32)
    Armament = models.CharField(max_length=255)
    Equipment = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tank(Common):
    Feature = models.CharField(max_length=255)


class Aircraft(Common):
    Feature = models.CharField(max_length=255)


class Helicopter(Common):
    Feature = models.CharField(max_length=255)


class Battleship(Common):
    Feature = models.CharField(max_length=255)


class Crew(Common):
    Expertise = models.CharField(max_length=64)
