
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from mail.views import SignUpView,LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPageView.as_view(),name='landingpage'),
    path('send_mail/',include("mail.urls", namespace='mails')),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignUpView.as_view(),name='signup'),
]
