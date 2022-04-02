
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from mail.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_mail/',include("mail.urls", namespace='mails')),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignUpView.as_view(),name='signup'),
    
]
