from django.urls import path
from django.views.generic import TemplateView

from view_app import views

app_name = 'view_app'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),

    path('hello_template/', views.hello_function_view, name='hello_template'),
    path('hello_template2/', views.HelloClassView.as_view(), name='hello_template2'),
    path('hello_template3/', views.HelloGenericView.as_view(), name='hello_template3'),
    # ciekawostka
    path('hello_template4/', TemplateView.as_view(template_name='view_app/hello.html'), name='hello_template4')
]
