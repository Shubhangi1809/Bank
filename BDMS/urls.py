from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="home/login.html"), name='EtBr-login'),
    path('t/<str:pk>/', views.Input),
    path('register/', views.register, name='EtBr-register'),
    path('accounts/profile/', views.index, name='EtBr-index'),
    path('maps/', views.maps, name='EtBr-maps'),
    path('profile/', views.profile, name='EtBr-profile'),
    path('reports/', views.reports, name='EtBr-reports'),
    path('help/', views.help, name='EtBr-help'),
    ]

if  settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  