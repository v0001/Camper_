from django.db import models

# Create your models here.
class MyPlace(models.Model):
    place = models.TextField()
    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    updated_at = models.DateField()

    def __str__(self):
        return self.place