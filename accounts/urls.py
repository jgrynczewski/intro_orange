from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    # Te endpointy powinny być w aplikacji account
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    # Te endpointy powinny być w innej aplikacji (bo nie dotyczą modelu użytkownika)
    # ale zostawiamy je tutaj, żeby tematy związane z uwierzytelnieniem i autoryzacją
    # były obok siebie.
    path('home/', views.home, name='home'),
    path('fun/', views.fun_view, name='test_view'),
    path('secret/', views.secret_view, name='secret_view'),
]