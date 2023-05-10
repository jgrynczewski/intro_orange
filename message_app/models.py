from django.db import models


class Message(models.Model):
    CHOICES = (
        ('question', 'pytanie'),
        ('other', 'inne'),
    )

    email = models.EmailField()
    category = models.CharField(max_length=100, choices=CHOICES)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    fav_date = models.DateField()
    fav_time = models.TimeField()

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
