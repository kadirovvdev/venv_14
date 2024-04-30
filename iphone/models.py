from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Create your models here.
