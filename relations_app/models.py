from django.db import models


# One-to-one (O2O)
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=100)
