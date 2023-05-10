from django.urls import path

from message_app import views

app_name = 'message_app'

urlpatterns = [
    path('contact1/', views.contact1, name='contact1')
]
