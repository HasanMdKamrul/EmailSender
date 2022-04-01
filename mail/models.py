from multiprocessing.dummy import Array
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class emails(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250)
    from_email = models.EmailField()
    cc_myself = models.BooleanField(default=False)
    cc_other_users = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    receiver_one = models.EmailField()
    receiver_two = models.EmailField(null=True, blank=True)
    receiver_three = models.EmailField(null=True, blank=True)
    receiver_four = models.EmailField(null=True, blank=True)
    receiver_five = models.EmailField(null=True, blank=True)
    
    
    def __str__(self):
        return self.subject