from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns =[
    path('', views.home, name="home"),
    path('predict/', views.predict, name="predict"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('registration/', views.RegistrationView.as_view(), name="registration"),
    path('login/', auth_view.LoginView.as_view(template_name ='login.html'), name="login")
]