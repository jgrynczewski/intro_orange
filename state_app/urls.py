from django.urls import path

from state_app import views

app_name = 'state_app'

urlpatterns = [
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('show-cookies/', views.show_cookies, name='show_cookies'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookies'),

    path('set-session/', views.set_session, name='set_session'),
    path('show-session/', views.show_session, name='show_session'),
    path('update-session/', views.update_session, name='update_session'),
    path('delet-session/', views.delete_session, name='delete_session'),
]