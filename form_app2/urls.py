from django.urls import path

from form_app2 import views

app_name = 'form_app2'

urlpatterns = [
    path('create/', views.create_task, name='create_task')
]