from django.urls import path

from form_app5 import views

app_name = 'form_app5'

urlpatterns = [
    path('create/', views.task_create_view, name='task_create_view'),
    path('list/', views.task_list_view, name='task_list_view'),
]