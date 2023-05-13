from django.urls import path

from message_app import views

app_name = 'message_app'

urlpatterns = [
    path('contact1/', views.contact1, name='contact1'),
    path('contact2/', views.contact2, name='contact2'),
    path('contact3/', views.contact3, name='contact3'),
]
