from django.urls import path

from form_app import views

app_name = 'form_app'

urlpatterns = [
    path('create/', views.create_task, name='create_task')
]