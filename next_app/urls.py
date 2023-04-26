from django.urls import path

from next_app import views


urlpatterns = [
    path('hello/', views.hello),
    path('hello/eva/', views.eva),
    path('hello/adam/', views.adam),
    path('hello/<str:data>/', views.name),

    path('hello2/', views.hello2),
    path('hello2/<str:data>/', views.name2),

    path('isitnewyear/', views.is_it_new_year),
    path('fruits/', views.fruits),
]
