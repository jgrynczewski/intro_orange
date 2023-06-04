import requests

from django.shortcuts import render


# Create your views here.
def dog_view(request):
    # połączenie z api
    api_response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = api_response.json()
    link = data.get('message')

    return render(
        request,
        'api_app/dogs.html',
        {
            'link': link
        }
    )
