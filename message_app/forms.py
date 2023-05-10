from django import forms


class MessageForm(forms.Form):
    CHOICES = (
        ('question', 'pytanie'),
        ('other', 'inne'),
    )

    email = forms.EmailField(label='Email')
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(label="Treść")
    fav_date = forms.DateField(label="Ulubiona data")
    fav_time = forms.TimeField(label="Ulubiony czas")
