from django.urls import path

from api_app import views


app_name = 'api_app'

urlpatterns = [
    path('', views.dog_view, name='dog_view'),
]
