
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_email/',include("mail.urls", namespace='mails')),
    path('login/', LoginView.as_view(), name='login'),
]
