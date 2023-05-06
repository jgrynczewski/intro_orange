from django.urls import path

from links import views

urlpatterns = [
    path('first/', views.first_view, name='first_name'),
    path('second/', views.second_view, name='second_name'),
    path('third/<str:param>/', views.third_view, name='third_name'),
]
