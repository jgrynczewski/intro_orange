from django.db import models


# One-to-one (O2O)
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=100)


# One-to-many (O2M)
class Language(models.Model):
    name = models.CharField(max_length=100)
    # framework_set =  # automatycznie dorobiony przez django menadżer powiązany


class Framework(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    # language_id = ...  # automatycznie dorobione przez django pole


class Actor(models.Model):
    name = models.CharField(max_length=100)
    # movie_set  # automatycznie dorobiony przez django menadżer powiązany


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField('Actor')  # i to też jest menadżer powiązany
