from django.urls import path

from next_app import views


urlpatterns = [
    path('hello/', views.hello),
    path('hello/eva/', views.eva),
    path('hello/adam/', views.adam),

    path('hello/<str:data>/', views.name),
]
