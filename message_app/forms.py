from django import forms


class MessageForm(forms.Form):
    CHOICES = (
        ('question', 'pytanie'),
        ('other', 'inne'),
    )

    email = forms.EmailField(label='Email')
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(
        label="Treść",
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 10})
    )
    fav_date = forms.DateField(
        label="Ulubiona data",
        widget=forms.NumberInput(attrs={'type': 'date'})
    )
    fav_time = forms.TimeField(
        label="Ulubiony godzina",
        widget=forms.NumberInput(attrs={'type': 'time'})
    )
