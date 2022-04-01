from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name="home/login.html"), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name="home/logout.html"), name='logout'),
    path('help/', views.help, name='help'),
    path('Loan/', views.Statement, name='reports'),
    path('registration/', views.registration, name='register'),
    path("contact/",views.Contact, name="Contact")
]
