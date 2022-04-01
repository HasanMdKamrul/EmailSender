

from django.urls import path
from .views import MailCreateView

app_name = 'mails'

urlpatterns = [

    path('', MailCreateView.as_view(), name='mail_create'),
    
]
