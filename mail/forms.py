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
        
        widgets = {
            'receiver_one': forms.EmailInput(attrs={'placeholder': 'Email Address One(*Required_field)'}),
            'receiver_two': forms.EmailInput(attrs={'placeholder': 'Email Address Two'}),
            'receiver_three': forms.EmailInput(attrs={'placeholder': 'Email Address Three'}),
            'receiver_four': forms.EmailInput(attrs={'placeholder': 'Email Address Four'}),
            'receiver_five': forms.EmailInput(attrs={'placeholder': 'Email Address Five'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type your Email here ...'}), 
            'subject': forms.TextInput(attrs={'placeholder': 'Type your Subject here ...'}),
        }

