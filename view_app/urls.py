from django.urls import path

from view_app import views

app_name = 'view_app'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
