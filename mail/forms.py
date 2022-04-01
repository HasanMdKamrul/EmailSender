from django import forms
from .models import emails



class MailCreateForm(forms.ModelForm):
    class Meta:
        model = emails
        fields = (
            'subject',
            'message',
            'receiver_one',
            'cc_myself',
            'cc_other_users',
            'receiver_two',
            'receiver_three',
            'receiver_four',
            'receiver_five',
        )

