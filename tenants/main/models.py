from django.db import models

# Create your models here.
class Types(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Houses(models.Model):
    type = models.ForeignKey(Types, on_delete=models.CASCADE, related_name="types")
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name