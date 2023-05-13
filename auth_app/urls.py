from django.urls import path

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]