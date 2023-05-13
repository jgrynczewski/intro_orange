from django import forms

from message_app.models import Message

# django form
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


# model form
class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        # fields = [
        #     'email',
        #     'category',
        #     ...
        # ]  # ew. exclude

        labels = {
            'email': "Email",
            'category': "Kategoria",
            'subject': 'Tytuł',
            'body': 'Treść',
            'fav_date': 'Ulubiona data',
            'fav_time': 'Ulubiona godzina'
        }
        widgets = {
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'fav_date': forms.NumberInput(attrs={'type': 'date'}),
            'fav_time': forms.NumberInput(attrs={'type': 'time'})
        }
