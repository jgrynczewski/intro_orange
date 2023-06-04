"""
URL configuration for intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from helo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('jurek/', views.jurek),
    path('hi/', views.hi),
    path('hi2/', views.hi2),

    path('next/', include('next_app.urls')),
    path('links/', include('links.urls')),
    path('inheritance/', include('inheritance.urls')),
    path('form/', include('form_app.urls')),
    path('form2/', include('form_app2.urls')),
    path('form3/', include('form_app3.urls')),
    path('form4/', include('form_app4.urls')),
    path('form5/', include('form_app5.urls')),
    path('crud/', include('crud_app.urls')),
    path('relations/', include('relations_app.urls')),
    path('message/', include('message_app.urls')),
    path('view/', include('view_app.urls')),
    path('state/', include('state_app.urls')),
    path('auth/', include('auth_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('dogs/', include('api_app.urls')),
]
